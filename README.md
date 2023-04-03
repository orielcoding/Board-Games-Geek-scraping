# Board-Games_Geek-scraping

This is a data mining project, so the main goal is to collect all the meangful data from the site 
"https://boardgamegeek.com/browse/boardgame".

BoardGameGeek (BGG) is a board game database - a collection or catalog of data and information on traditional board games. The game information recorded there is intended for posterity, historical research, and user-contributed ratings. 

By scraping the data and analysing it we hope to get valuable insights into board game industry and players preferencies, and may be select a few new games for ourselves. 


Usage:
- download the bgg.sql file
- login to your mysql user, and type in mysql the following query (choose name for the database): "CREATE DATABASE databasename;"
- from the cmd run the following line (your username and the databasename you chose): "mysql -u username -p databasename < bgg.sql" 
- change the following value of "SQLAlchemy_db_connection" key in configuration.json file to your username, password, localhost and database name
where the sql database is located. example: "mysql+pymysql://username:password@host/database"
- install all the packages in the requirements file. 
- Thats it! go ahead and start scraping bgg


At the current stage the code:
* collects individual game's ULS
* goes to each URL and scraps the information on:
    * game title and release date
    * game play
    * game features
    * game creators
    * game stats

The code is wrapped up with decorator which logs exceptions and prints them to file ("bgg_exception.log")

It is possible to run the code from command line with different arguments (providing number of games to scrape, specifying the information which has to be collected and stating that the information scraped  should be written to database):

# Prerequisites
see requirements.txt


# Authors
Oriel Singer (https://www.linkedin.com/in/oriel-singer/)

Maria Blinchevskaya (https://www.linkedin.com/in/maria-blinchevskaya/)

