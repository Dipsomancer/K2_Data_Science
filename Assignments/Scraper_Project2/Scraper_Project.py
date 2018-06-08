import requests
import datetime

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
User_County = '{county}'.format(**political)

# Create Current Timstamp

currentDT = str(datetime.datetime.now())


# Connecting to the database file
conn = sqlite3.connect('County_DB.sqlite') #put in with statement and then put in an except with a close at end
c = conn.cursor()

#Wikipedia_Table
c.execute('SELECT * FROM WIKIPEDIA_TABLE WHERE County_Name = ?',(User_County,))
wiki_entry = c.fetchone()

#Write Output back to TABLE
c.execute("INSERT INTO USER_ENTRY_TABLE (Entry_ID, User_Address, Entry_Timestamp, County_Name, FIPS_Code, County_Seat, Created, Formed_From, Named_For, Density, Pop_2010, Area) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",('1', ADDRESS, currentDT, wiki_entry[0], wiki_entry[1], wiki_entry[2], wiki_entry[3], wiki_entry[4], wiki_entry[5], wiki_entry[6], wiki_entry[7], wiki_entry[8]))

#Select Entry From User Table and Return to User
c.execute('SELECT * FROM USER_ENTRY_TABLE')
user_entry = c.fetchone()
print('Your County is: ' + user_entry[3] + '\n' + 'Established: ' + user_entry[6] + '\n' + 'County Seat: ' + user_entry[5] + '\n' + 'Density: ' + user_entry[9] + '\n' + 'Population in 2010: ' + user_entry[10] + '\n' + 'Area: ' + user_entry[11])

conn.commit()
conn.close()
