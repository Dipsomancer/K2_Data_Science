'''
import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

params = {
    'address': '524 4th Avenue, Brooklyn, United States',
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

import lxml
import wikipedia
import pandas as pd

from bs4 import BeautifulSoup

#https://en.wikipedia.org/wiki/List_of_counties_in_New_York

New_York = wikipedia.WikipediaPage(pageid = 82159)

#print(New_York.html())

soup = BeautifulSoup(New_York.html(), 'html.parser')

#print(soup.prettify())

#print(soup.find_all('a'))

#for county in soup.find_all('a'):
#    if county.parent.name == 'li':
#        print (county["title"])

table = soup.find_all('table')[2]

#print(table.a['title'])
#for county in soup.find_all('table')[2]:
#    if county.parent.name == 'td':
#        print (county["title"])

new_table = pd.DataFrame(columns = range(0,10), index = [0])

#new_table = pd.DataFrame(size = (10,62), columns=['County','FIPS Code','County seat','Created','Formed from','Named for','Density','2010 Population','Area','Map'])


#row_marker = 0
#for row in table.find_all('tr'):
#    column_marker = 0
#    columns = row.find_all('td')
#    for column in columns:
#        new_table.iat[row_marker,column_marker] = column.get_text()
#        column_marker += 1

#print(new_table)
new_york_table = []

for table_row in table.find_all('tr'):
    new_york_table.append(table_row.text)
    row_in_data = []
    for cell in table_row.find_all('td'):
        row_in_data.append(cell.text.strip())#.encode('utf-8'))
    new_york_table.append(row_in_data)

print(new_york_table)

#for row in table.find_all('tr'):
#    column_marker = 0
#    columns = row.find_all('td')
#    for column in columns:
#        print(column.find_all('a'))

#for link in table.find_all('a'):
#    print(link.get('title'))

#print(table)

'''
data = []
table = soup.find('table' attrs = {'class':'wikitable sortable jquery-tablesorter'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
'''
#for county in soup.find_all('a'):
#    if county.parent.name == 'title.wikitable.sortable.jquery-tablesorter':
#        print (county["title"])

#SQL
'''
import sqlite3

sqlite_file = 'my_db.sqlite'
conn = sqlite3.connect(sqlite_file)

c = conn.cursor()

#where the database file (sqlite_file) can reside anywhere on our disk, e.g.,


sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'  # name of the table to be created
table_name2 = 'my_table_2'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))

# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

# A) Inserts an ID with a specific value in a second column
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# B) Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))

# C) Updates the newly inserted or pre-existing entry
c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)".\
        format(tn=table_name, cn=column_name, idf=id_column))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
'''
