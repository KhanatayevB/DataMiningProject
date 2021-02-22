# DataMiningProject

This is a project to learn and apply web scraping to some website that 
contains a lot of data. 

#Website 
The website that we chose is: https://www.basketball-reference.com/ \
The website for the particular table in NBA_SCRAPER-CP1 is: https://www.basketball-reference.com/leagues/NBA_2021.html#team-stats-base \
The table is called Team Stats, the url for the embedded table is: https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2021.html&div=div_team-stats-base \

#Approach

The first step to creating this scraper is to learn the BeautifulSoup package and some\
basic html. The url used in the CP1 file is embedded and makes things easier.\
However, the scraper should ideally be more robust. \

Once the data is retrieved from the table, the data from each row is read and stored in \
a two dimensional list. The title row is also stored. \
The data is then configured into a DataFrame and printed out. 

# Execution

To run the code, make sure that everything is installed per the requirements.txt file \
Choose a table on the website, click on it and find the embed link\
Simply assign it to the url variable as a string, just like the default

# Contributors

This project is owned by: \
Bazham Khanatayev \
Ben Hendel

# GitHub Link

This project is in a public repository: \
https://github.com/KhanatayevB/DataMiningProject


# Project Status

Checkpoint 1 - basic webscrape working, project set up