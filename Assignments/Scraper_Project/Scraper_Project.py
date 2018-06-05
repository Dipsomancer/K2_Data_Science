'''
import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

ADDRESS = input('What is you address (For example --> 524 4th Avenue, Brooklyn, United States)? ')

params = {
    'address': ADDRESS,
    'sensor': 'false',
    'region': 'us'
}

# Do the request and get the response data
req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json() # .json() = JSON decoder

# Use the first result
result = res['results'][0]

political = dict()
political['county'] = result['address_components'][4]['long_name']
print('{county}'.format(**political)) #Review

#print(res)

'''
#Wikipedia
'''
import lxml
import wikipedia
import pandas as pd

from bs4 import BeautifulSoup

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

print(new_york_table)
'''
#SQL

import sqlite3
import datetime
#Create Database and Tables if they don't exist

#Create Wikipedia Table and User Entry Table

currentDT = str(datetime.datetime.now())
print(currentDT)
# Connecting to the database file
conn = sqlite3.connect('County_DB.sqlite') #put in with statement and then put in an except with a close at end
c = conn.cursor()

#Wikipedia_Table
c.execute('CREATE TABLE WIKIPEDIA_TABLE (County_Name TEXT PRIMARY KEY, FIPS_Code TEXT, County_Seat TEXT, Created TEXT, Formed_From TEXT, Named_For TEXT,Density TEXT, Pop_2010 TEXT, Area TEXT)')

#User Entry Table
c.execute('CREATE TABLE USER_ENTRY_TABLE (Entry_ID INTEGER PRIMARY KEY AUTOINCREMENT, User_Address TEXT, Entry_Timestamp Timestamp, County_Name TEXT, FIPS_Code TEXT, County_Seat TEXT, Created TEXT, Formed_From TEXT, Named_For TEXT,Density TEXT, Pop_2010 TEXT, Area TEXT)')

#Practice Write
c.execute("INSERT INTO WIKIPEDIA_TABLE (County_Name, FIPS_Code, County_Seat, Created, Formed_From, Named_For, Density, Pop_2010, Area) VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9')")

conn.commit()
conn.close()
