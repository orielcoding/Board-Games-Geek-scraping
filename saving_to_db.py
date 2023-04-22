from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import select
import bs4
import json

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)

# Create a MySQL engine
engine = create_engine(config['SQLAlchemy_db_connection'])


def connect_to_db_tables() -> dict:
    """
    This function reflects database, recreate the tables from it, and return them.
    """

    # Create a metadata instance
    metadata = MetaData()

    # Reflect the database schema
    metadata.reflect(bind=engine)

    # Get the table instances
    table_names = metadata.tables.keys()

    # Create a dictionary to store the table objects
    tables = {}

    # Loop through the table names and add the table objects to the dictionary
    for table_name in table_names:
        tables[table_name] = metadata.tables[table_name]

    # This lines show relationsheeps between tables by foreign keys.
    # for table_name, table in tables.items():
    #     for column in table.columns:
    #         for fk in column.foreign_keys:
    #             print(f"Table {table_name} has a foreign key constraint on column {column.name} "
    #                   f"which references {fk.column.table.name}.{fk.column.name}")

    return tables


def normalize_single_obj(obj_features: list) -> list:
    """
        This function normalize single object in a recursive way. it takes each column of object's given data, and
        seperate it to have single values.
        The function returns list of normalized rows of the object.
        """
    normalized_rows: list = []
    for index, column in enumerate(obj_features):
        # normalize only if the Game attribute is a container (has multiple values).
        if not isinstance(column, (str, bs4.element.NavigableString, int, float)) and column is not None:
            for col_index, value in enumerate(obj_features[index]):
                split_obj = obj_features[:index] + [value]
                if index != len(obj_features) - 1:
                    split_obj += obj_features[index + 1:]
                normalized_rows += normalize_single_obj(split_obj)
            return normalized_rows
    return [obj_features]


def normalize_objects(obj_values_lst: list) -> list:
    """
    This func normalize all the objects. it sends single object to subfunction each time.
    """
    normalized_list = []
    for obj in obj_values_lst:
        if type(obj) is str or type(obj) is int or type(obj) is float:
            obj = list(obj)
        normalized_list += normalize_single_obj(obj)
    return normalized_list


def select_fk(conn: engine, normalized_rows: list, table, table_fk_col: str, table_value_col: str, value_col: int) -> list:
    """
    This function changes the normalized rows to have foreign keys in relevant places instead of explicit values.
    params:
            table - Table to inherit ID from.
            table_fk_col - The column name which is used as the fk (ID column mostly).
            table_value_col - The column name in the table which we need to search the given value from the row.
            value_col - The column index of the Game attributes which value we need to extract and replace with the fk.
    returns: the row with the fk (mostly ID) instead of the non-unique value.
    """

    for index, row in enumerate(normalized_rows):
        value = row[value_col]
        query = select(table.columns[table_fk_col]).where(table.columns[table_value_col] == value)
        # if str(table.name) == 'game_reimplements' and not conn.execute(query).fetchone():
        table_identifier: int = conn.execute(query).fetchone()[0]
        normalized_rows[index][value_col] = table_identifier
    return normalized_rows


def insert_to_db(table: MetaData, obj_normalized_list: list, conn: engine, unique_col: str = None) -> None:
    """
    This function accepts list of normalized rows and saves them to db in relevant tables, while preventing duplicates.
    """

    # check if table has pk which is auto increment
    has_pk: bool = bool(table.primary_key)
    is_autoincrement: bool = False
    if has_pk:
        pk_col = table.primary_key.columns.values()[0]
        is_autoincrement = pk_col.autoincrement

    # saving data into db. The data inserted as table rows with the relevant Game attributes for each row.
    for row in obj_normalized_list:
        data_dict: dict = {}
        delay = 0  # In case a table has autoincrement column, delay will correlate data col index and table col index.
        if is_autoincrement:
            delay = 1

        # Iterating over each Game attribute to enter it to the correct column of the table.
        for i in range(delay, len(table.columns)):
            # prevent duplicates
            if table.columns[i].name == unique_col:
                if conn.execute(
                        table.select().where(table.columns[unique_col] == row[i - delay])).fetchall() and unique_col:
                    break  # skipping row because the unique value already appears in the table.
            data_dict[table.columns[i]] = row[i - delay]  # key is column name of table
        if data_dict != {}:
            conn.execute(table.insert().values(data_dict))
            conn.commit()


def data_to_db(table: MetaData, obj_values_lst: list, unique_column: str = None, inherit_from=None,
               match_fk_col: list = None, match_val_col: list = None, replace_val_col: list = [1]):
    """
    This is the main function. it accepts all required values for all the functions it calls.
    The data pass through multiple processing function until eventually it is saved to database in 1NF form.
    """
    with engine.connect() as conn:

        # normalize each object to 1NF form
        normalized_objects: list = normalize_objects(obj_values_lst)

        if inherit_from:  # then match_col and fk_col must be filled also.
            # replace values with fk (ID's).
            try:
                assert len(inherit_from) == len(match_fk_col)
                assert len(inherit_from) == len(replace_val_col)
            except AssertionError as e:
                print('The shapes of columns to inherit from and columns to check their values dont match.')
                return
            for i in range(len(inherit_from)):
                normalized_objects = select_fk(conn, normalized_objects, inherit_from[i], match_fk_col[i], match_val_col[i], replace_val_col[i])

        insert_to_db(table, normalized_objects, conn, unique_column)


def describe_table(table: MetaData):
    """
    This function display data of specific table in db.
    """

    # select all columns in the table
    select_query = select(table.columns)

    with engine.connect() as conn:
        # execute the query and get the rows
        rows = conn.execute(select_query).fetchall()

    # print the rows
    for row in rows:
        print(row)
