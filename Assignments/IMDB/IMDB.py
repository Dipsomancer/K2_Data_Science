#Import Modules and CSV data

import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')

credits = pd.read_csv('tmdb_5000_credits.csv')

#pd.set_option('display.max_colwidth', -1)

#print(credits.head())

#print(movies.head())

#credits.head()

#movies.dtypes

#budget                    int64
#genres                   object
#homepage                 object
#id                        int64
#keywords                 object
#original_language        object
#original_title           object
#overview                 object
#popularity              float64
#production_companies     object
#production_countries     object
#release_date             object
#revenue                   int64
#runtime                 float64
#spoken_languages         object
#status                   object
#tagline                  object
#title                    object
#vote_average            float64
#vote_count                int64

#credits.dtypes

#movie_id     int64
#title       object
#cast        object
#crew        object

#credits[credits.movie_id==19995].title.values

# .values will convert panda to numpy dataframe

#credits[credits.movie_id==19995].title.iloc[0]


'''
import ast
import itertools

x = credits.loc[credits['movie_id'] == [19995]]['cast'][0]
x = ast.literal_eval(x)

y = movies[['revenue','id','genres']]
k = movies['genres']
k['genres'] = ast.literal_eval(k[0])

#print(x)
#print(y)
print(k['genres'][0]['id'])
'''

import json

movies['genres'] = movies['genres'].apply(json.loads)

#Helper Function for turning nested JSON-ish column into list with desired fields

def list_from_json(table_name, column_field, field_variable):
    i = []
    for a, row in table_name.iterrows():
        i.append([column_field[field_variable] for column_field in row[1]])
    return i

#Run helper function for 'genres' field and create 'test' field

movies['test'] = list_from_json(movies, 'genres', 'name')

#Convert list to a set of distinct values (genres) to iterate over

genres_set = set(x for l in movies['test'] for x in l)

#Create Dictionary from set list, with default value of 0

genres_dictionary = dict.fromkeys(genres_set,0)

#Iterate over genres set list, and then genres in 'test' column to get total revenue by genre

for i in genres_set:
    for index, r in movies.iterrows():
        if i in r['test']:
            genres_dictionary[i] += r['revenue']

#Since dictionaries can't be indexed on, import operator library

import operator

#Sort genres dictionary on revenue, and return sorted list

genres_dictionary_s = sorted(genres_dictionary.items(), key=operator.itemgetter(1))

#print(genres_dictionary_s)



# **Question 1**
#How does gross revenue vary for genre?
'''
[('TV Movie', 0), ('Foreign', 12398151), ('Documentary', 1082277678), ('Western', 3792169111), ('Music', 8964351078), ('History', 11332141732), ('War', 12118445911), ('Horror', 22599894663), ('Mystery', 27248722761), ('Crime', 46040860686), ('Animation', 52812167865), ('Romance', 53642137545), ('Science Fiction', 81564235745), ('Fantasy', 81982199925), ('Family', 83283238689), ('Thriller', 103250426269), ('Drama', 119710983984), ('Comedy', 122760517608), ('Action', 162959914515), ('Adventure', 164841561551)]
'''
#...content rating (R, PG13, etc.)?

#Not a part of the updated data sets! :/

#Facebook likes?

#Same as above! :/

#budget?

#Try correlation to see relationship?

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#sns.jointplot(data=movies, x='revenue', y='budget', kind='reg', color='g')
#plt.show()

#Revenue and Budget have a positive correlation .73 (Pearson), so is statistially significant given the sample size but may not be meaningful

#cast total likes?

#IMDB likes?

#Not in data set

#Not in set, using popularity

#sns.jointplot(data=movies, x='revenue', y='popularity', kind='reg', color='g')
#plt.show()

#Again, correlation (.64).  Some outliers with 400+ rating may skew data set, but no reason to remove

#In general, how are these variables related to each other? For example, do social media likes align with critic’s views?

movies_01 = movies[['budget', 'popularity', 'revenue', 'runtime']].copy()

#print(movies_01.describe())

#print(movies_01.corr())

#No significant correlations other than what was refferenced above

###movies.isnull().sum()

# Some Homepages, Overviews, Release Dates, Runtimes, and Taglines missing, but no NULLs in other areas...

# **Question 2** – What famous actors and directors have the highest budget to gross ratio?
#
# **Details** – When a studio spends money on a big name they expect it to greatly increase their revenue, but is this always the case? After selecting actors and directors that appear frequently in the dataset, who is the most worth it? Do these actors and directors consistently appear in one genre or are they profitable across various genres?

#Creare new data frame joining credits and movies

pd.options.mode.chained_assignment = None

Test = pd.merge(movies, credits,left_on=['id'], right_on=['movie_id'], how='inner')

Test2 = Test[['budget','revenue','crew','cast']]

#Test2['crew'] = Test2['crew'].apply(json.loads)


count = 1

for index, row in Test2.iterrows():
    #try:
    print(type(row[2]))
    Test2['crew'][index] = json.loads(row[2])
    print(type(row[2]))
    break

    #except:
    print(str(count))
    count += 1
    print('Data failure')
    break

def list_from_json2(table_name, column_field, field_variable):
    i = []
    for a, row in table_name.iterrows():
        i.append([column_field[field_variable] for column_field in row[20]])
    return i


###Test2['crew'] = list_from_json2(Test2, 'crew', 'Director')

#"job": "Director", "name": ""

#movies['crew'] = list_from_json(Test2, 'crew', 'Director')

#print(Test2.loc['crew'][1]['Director'])

'''
#Convert list to a set of distinct values (genres) to iterate over

genres_set = set(x for l in movies['test'] for x in l)

#Create Dictionary from set list, with default value of 0

genres_dictionary = dict.fromkeys(genres_set,0)

#Iterate over genres set list, and then genres in 'test' column to get total revenue by genre

for i in genres_set:
    for index, r in movies.iterrows():
        if i in r['test']:
            genres_dictionary[i] += r['revenue']

#Since dictionaries can't be indexed on, import operator library

import operator

#Sort genres dictionary on revenue, and return sorted list

genres_dictionary_s = sorted(genres_dictionary.items(), key=operator.itemgetter(1))

#print(genres_dictionary_s)

'''

# **Question 3** – What movies where the biggest flops? Are there factors that are associated with flops?
#
# **Details** – Given both budget and gross data can you quantify this? Remember the note that some movies may be in different currencies.
