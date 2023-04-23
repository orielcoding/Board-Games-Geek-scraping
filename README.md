# Board-Games_Geek-scraping

This is a data mining project, so the main goal is to collect all the meangful data from the site 
"https://boardgamegeek.com/browse/boardgame".

BoardGameGeek (BGG) is a board game database - a collection or catalog of data and information on traditional board games. The game information recorded there is intended for posterity, historical research, and user-contributed ratings. 

By scraping the data and analysing it we hope to get valuable insights into board game industry and players preferencies, and may be select a few new games for ourselves. 


**How to run the code**:
- download the bgg.sql file
- login to your mysql user, and type in mysql the following query (choose name for the database): "CREATE DATABASE bgg_db;"
- from the cmd run the following line (your username): "mysql -u username -p bgg_db < bgg.sql" 
- Open the 'BGG_configuration.json' file, and change the value of "SQLAlchemy_db_connection" key to your username, password, localhost and database name
where the sql database is located. example: "mysql+pymysql://username:password@host/database"
- install all the packages in the requirements file. 


The code is wrapped up with decorator which logs exceptions and prints them to file ("bgg_exception.log").

It is possible to run the code from command line with different arguments (providing number of games to scrape, specifying the information which has to be collected, get game prices from an API, and stating that the information scraped  should be written to database).

*Note*: to save scraped data into database you must scrape the entire data (default option).


# Prerequisites
see requirements.txt


# Authors
Oriel Singer (https://www.linkedin.com/in/oriel-singer/)

Maria Blinchevskaya (https://www.linkedin.com/in/maria-blinchevskaya/)

