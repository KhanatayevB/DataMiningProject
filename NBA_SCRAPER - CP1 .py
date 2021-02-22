"""Bazham Khanatayev, Ben Handel
    Data Mining Project Checkpoint 1"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# The following URL points towards the specific table that we are scraping. It was retrieved as code that is used to
# embed the table in another website. The website has options to provide a link of that sort. If we want to access
# different tables on the website, we can just use the corresponding embedded code
url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_2021.html&div=div_team-stats" \
      "-per_game "

html = requests.get(url)  # the requests library is used to send http requests, and to access the site. This works
# better than the urllib requests library

soup = BeautifulSoup(html.content)  # BeautifulSoup object is created by passing function through our table source code

# When we inspect the element on the website, we can see that the "tr" refers to the table rows, the next line of code
# grabs all of the rows in html format where each row is separated by <> symbols
rows = soup.findAll('tr')[1:] # when inspecting the element, you can see that the first "td" is empty. So, we do
# not want to use it. It makes the final output have a 0 row filled with "None" elements

# For this next part we see that each row is a "tr" which is made up of many "td" objects. Each "td" is a specific
# statistic for the corresponding "tr" that it is under. We pass through each row and we grab the data from all of the
# td objects in that row.
team_stats = [[td.getText() for td in rows[i].findAll('td')]  # grabs all of the "td" objects from a row, and then grabs
              # all of the individual data points by passing each "td" through the getText() method
              for i in range(len(rows))]  # lets us know how many rows we must go through
# team_stats is now a list where the first element is an empty list. The rest of the elements are lists of strings where
# each string corresponds to a statistic in a specific order


# We have all of the body information needed to create a DataFrame. But, we also need the headers. This is done
# similarly to getting all of the rows. But, we only need row 0.
column_names = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
column_names = column_names[1:]  # The first element in headers, similar to team_stats, is an empty list. We need to
# ignore this
# one since our data starts at element 1. We know have a list of the column names that correspond to the positions of
# the output in team_stats

pd.set_option('display.max_columns', None) # this code allows us to see all of the columns that are outputted
output = pd.DataFrame(team_stats, columns=column_names) # a Dataframe is created with our list of lists (2D frame) and
# the column titles are set to our column_names list
print(output)
