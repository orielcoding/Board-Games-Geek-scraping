# Board-Games_Geek-scraping

This is a data mining project, so the main goal is to collect all the meangful data from the site 
"https://boardgamegeek.com/browse/boardgame".

BoardGameGeek (BGG) is a board game database - a collection or catalog of data and information on traditional board games. The game information recorded there is intended for posterity, historical research, and user-contributed ratings. 

By scraping the data and analysing it we hope to get valuable insights into board game industry and players preferencies, and may be select a few new games for ourselves. 


At the current stage the code:
* collects individual game's ULS
* goes to each URL and scraps the information on:
** game title and release date
** game play
** game features
** game creators
** game stats

The code is wrapped up with decorator which logs exceptions and prints them to file ("bgg_exception.log")

It is possible to run the code from command line with different arguments (providing number of games to scrape, specifying the information which has to be collected and stating that the information scraped  should be written to database):

  -n NUM_GAMES, --num_games NUM_GAMES
                        specifies number of pages to scrap
  -s, --stats           limits data collection to stats
  -c, --creators        limits data collection to info on creators
  -g, --gameplay        limits data collection to info on gameplay
  -f, --features        limits data collection to info about features
  -d, --database        to save the info into sql database

Prerequisites
see requirements.txt


Authors
Oriel Singer ()

Maria Blinchevskaya (https://www.linkedin.com/in/maria-blinchevskaya/)

