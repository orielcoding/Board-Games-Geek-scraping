# Board-Games_Geek-scraping

This is a data mining project, so the main goal is to collect all the meaningful data from the site 
"https://boardgamegeek.com/browse/boardgame".

BoardGameGeek (BGG) is a board game database - a collection or catalog of data and information on traditional board games. The game information recorded there is intended for posterity, historical research, and user-contributed ratings. 

By scraping the data and analysing it we hope to get valuable insights into board game industry and players preferences, and may be select a few new games for ourselves. 


**How to run the code**:
- Open the 'BGG_configuration.json' file, and change the value of "SQLAlchemy_db_connection" key to your username, password, localhost and database name where the sql database is located. example: "mysql+pymysql://username:password@host/database";
- install all the packages in the requirements file;
- run the main code file ("scraping_bgg.py") from the command line
- example of how the command should look like: python scraping_bgg.py -n NUM_GAMES -d (to scrape and write NUM_GAMES to db)

It is possible to run the code with different arguments (providing number of games to scrape, specifying the information which has to be collected (e.g. creators, features etc.), get game prices from an API, and stating that the information scraped  should be written to database).

*Note*: if you want to save scraped data into database you can still select number of games to scrape, but must scrape all the available pieces of information (default option).

The code is wrapped up with decorator which logs the progress of the code execution and exceptions (if any) and prints them to file ("bgg_scraping.log").


# Prerequisites
use requirements.txt


# Authors
Oriel Singer (https://www.linkedin.com/in/oriel-singer/)

Maria Blinchevskaya (https://www.linkedin.com/in/maria-blinchevskaya/)

