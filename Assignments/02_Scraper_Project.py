'''

import requests

#response = requests.get("http://api.open-notify.org/iss-now.json")

#print(response.status_code)

params = {appShortName: null, systemID: '', masterPassword: '', APIPacketID: '', SinceDateTimeStamp: '2018-01-01'}

response = requests.get("https://prmois.cleverex.com/promis_agencywebservice/PDEP.asmx?op=GetPDEPPrograms")
#getPDEPPrograms(appShortName, systemID, masterPassword, APIPacketID, SinceDateTimeStamp)
print(response.status_code)

short name = edalliance
key = _BNp#LD:N>2R(f7EX_smtwk.4(_B{hK@K


'''

#API Section

# References:

# http://docs.python-requests.org/en/latest/
# https://developers.google.com/maps

# http://www.yelp.com/developers/documentation/v3/get_started
'''
import requests

#GET https://api.yelp.com/v3/business/{id}

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

params = {
    'address': '221B Baker Street, London, United Kingdom',
    'sensor': 'false',
    'region': 'uk'
}

# Do the request and get the response data
req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json()


#Use the first result
result = res['results'][0]

geodata = dict()
geodata['lat'] = result['geometry']['location']['lat']
geodata['lng'] = result['geometry']['location']['lng']
geodata['address'] = result['formatted_address']

print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))

'''
#Wikipedia

'''
import wikipedia

print (wikipedia.summary("Wikipedia"))
# Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...

wikipedia.search("Barack")
# [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']

ny = wikipedia.page("New York")
ny.title
# u'New York'
ny.url
# u'http://en.wikipedia.org/wiki/New_York'
ny.content
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
ny.links[0]
# u'1790 United States Census'

wikipedia.set_lang("fr")
wikipedia.summary("Facebook", sentences=1)
'''

#SQL

import sqlite3

#sqlite_file = 'my_db.sqlite'

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
'''
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
