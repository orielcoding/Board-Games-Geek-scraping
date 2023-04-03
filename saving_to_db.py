from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence
from sqlalchemy import select, exists
import json

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)

# Create a MySQL engine
engine = create_engine(config['SQLAlchemy_db_connection'])


def connect_to_db_tables() -> dict:
    """
    This function reflects and prepare the tables from the requested db to start saving data in them, and returns
    the tables.
    """

    # Create a metadata instance
    metadata = MetaData()

    # Reflect the database schema
    metadata.reflect(bind=engine)

    # Get the table instances
    table_names = metadata.tables.keys()
    # tables: dict = {table_name: metadata.tables[table_name] for table_name in table_names}

    # Create a dictionary to store the table objects
    tbls = {}

    # Loop through the table names and add the table objects to the dictionary
    for table_name in table_names:
        tbls[table_name] = metadata.tables[table_name]

    return tbls


def saving_independent_tables_info(table: MetaData, obj_values_lst: list, unique_column_name: str):
    """
    Params: table - the desired table to insert values to.
            obj_value_lst - list of all relevant columns of all desired objects to insert into the table.
                            **The parameter either contain multiple single values inside list, or a single
                            container inside the list with multiple values.
            unique_column_name - column by which the sqlalchemy engine will prevent duplicates in the table.
    The function saves objects info into independent table
    """

    # Define the data to be inserted as a list of dictionaries
    if len(obj_values_lst) == 1:
        obj_values_lst = obj_values_lst[0]  # in case it has container inside instead of multiple single values.

    with engine.connect() as conn:
        for obj in obj_values_lst:
            data_dict: dict = {}
            if type(obj) is str:
                data_dict[table.columns[1]] = obj
            else:
                for value in obj:  # actually works if there is only one column in the table with multiple values!
                    for index, column in enumerate(table.columns):
                        if index == 0:
                            continue  # skip auto-increment columns
                        data_dict[column.name] = value

                # check if the row already exists before inserting
                print(data_dict)
                if not conn.execute(table.select().where(table.c[unique_column_name] == value)).fetchall():
                    conn.execute(table.insert().values(data_dict))
                    conn.commit()


def saving_to_first_level_relational_tables(table: MetaData, obj_values_lst: list, inherit_from: MetaData):
    """
    Params: table - the desired table to insert values to.
            obj_value_lst - list of all relevant columns of all desired objects to insert into the table.
                            **The parameter either contain multiple single values inside list, or a single
                            container inside the list with multiple values.
            inherit_from - Metadata table which the foreign key points at.

    The function saves objects info into independent table
    """

    # Define the data to be inserted as a list of dictionaries
    if len(obj_values_lst) == 1:
        obj_values_lst = obj_values_lst[0]  # in case it has container inside instead of multiple single values.

    with engine.connect() as conn:
        for obj in obj_values_lst:
            title: str = obj[0]
            print(inherit_from.columns.name)
            game_id = conn.execute(select([inherit_from.columns.id]).where(inherit_from.columns.name == title)).scalar()
            obj[0] = game_id
            data_dict: dict = {}
            for index, column in enumerate(table.columns):
                data_dict[column.name] = obj[index]

            # check if the row already exists before inserting
            if not conn.execute(table.select().where(table.c.id == obj[0])).fetchall():
                conn.execute(table.insert().values(data_dict))
                conn.commit()


def describe_table(table: MetaData):
    # select all rows in the table
    select_query = select(table.columns)

    with engine.connect() as conn:
        # execute the query and get the rows
        rows = conn.execute(select_query).fetchall()

    # print the rows
    for row in rows:
        print(row)
