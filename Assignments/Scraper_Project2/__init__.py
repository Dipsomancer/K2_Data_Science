#Wikipedia

import lxml
import wikipedia
import pandas as pd
import sqlite3

from bs4 import BeautifulSoup

#Query Wikipedia and Prepare Data Table

#https://en.wikipedia.org/wiki/List_of_counties_in_New_York

New_York = wikipedia.WikipediaPage(pageid = 82159)

soup = BeautifulSoup(New_York.html(), 'html.parser')

table = soup.find_all('table')[2]

new_york_table = []

for table_row in table.find_all('tr'):
    row_in_data = []
    for cell in table_row.find_all('td'):
        if cell == None:
            continue
        if cell.span:
            cell.span.decompose()
        row_in_data.append(cell.find(text=True).strip().replace(u'\xa0',' '))
    new_york_table.append(row_in_data)

new_york_table.pop(0)

#SQL

#Create Database and Tables if they don't exist

# Connecting to the database file
conn = sqlite3.connect('County_DB.sqlite') #put in with statement and then put in an except with a close at end
c = conn.cursor()

#Wikipedia_Table
c.execute('CREATE TABLE WIKIPEDIA_TABLE (County_Name TEXT PRIMARY KEY, FIPS_Code TEXT, County_Seat TEXT, Created TEXT, Formed_From TEXT, Named_For TEXT,Density TEXT, Pop_2010 TEXT, Area TEXT)')

#User Entry Table
c.execute('CREATE TABLE USER_ENTRY_TABLE (Entry_ID INTEGER PRIMARY KEY AUTOINCREMENT, User_Address TEXT, Entry_Timestamp Timestamp, County_Name TEXT, FIPS_Code TEXT, County_Seat TEXT, Created TEXT, Formed_From TEXT, Named_For TEXT,Density TEXT, Pop_2010 TEXT, Area TEXT)')

#Write new_york_table from Wikipedia call into WIKIPEDIA_TABLE
for r in new_york_table:
    c.execute("INSERT INTO WIKIPEDIA_TABLE (County_Name, FIPS_Code, County_Seat, Created, Formed_From, Named_For, Density, Pop_2010, Area) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))

conn.commit()
conn.close()
