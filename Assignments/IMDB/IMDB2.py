
# coding: utf-8

# *Module 2 Final Project: IMDB Dataset*

# In[1]:


#Import Modules and CSV data

import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')

credits = pd.read_csv('tmdb_5000_credits.csv')

#pd.set_option('display.max_colwidth', -1)

#print(credits.head())

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


# In[25]:
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
#print(type(movies['genres'][0][0]))
##print(movies['genres'][0])

#for i in movies['genres'][0]:
#    print(i['name'])
'''
for a, row in movies.iterrows():
    print(type(row))
    for i, cell in enumerate(row):
        print(i)
        print(cell)
    print([genres['name'] for genres in row[1]])
    break

def list_from_json(table_name, column_field, field_variable):
    for a, row in table_name.iterrows():
        return [column_field[field_variable] for column_field in row[1]]
'''

def list_from_json(table_name, column_field, field_variable):
    i = []
    for a, row in table_name.iterrows():
        i.append([column_field[field_variable] for column_field in row[1]])
    return i

#print(list_from_json(movies, 'genres', 'name'))

movies['test'] = list_from_json(movies, 'genres', 'name')
#movies['test'] = 'abc'

print(movies.head())

# **Question 1** – How does gross revenue vary for genre, content rating (R, PG13, etc.), Facebook likes, budget, cast total likes, IMDB likes, etc.?  In general, how are these variables related to each other? For example, do social media likes align with critic’s views?
#
# **Details** – These kinds of questions influence how much a movie studio might want to spend on social media marketing, on actors, on their budget, or in reaching out to critics to review movies. With evidence from data, decision makers are better able to understand how to meet their objectives. The column genre represents a list of genres associated with the movie in a string format separated by | . Write code to parse each text string into a binary vector with 1s representing the presence of a genre and 0s the absence, and add it to the DataFrame as additional columns. This may help you explore gross revenue as a function of genre. Many of the other features are numerical and lend themselves to scatterplots.

# In[7]:


###movies.isnull().sum()


# Some Homepages, Overviews, Release Dates, Runtimes, and Taglines missing, but no NULLs in other areas...

# **Question 2** – What famous actors and directors have the highest budget to gross ratio?
#
# **Details** – When a studio spends money on a big name they expect it to greatly increase their revenue, but is this always the case? After selecting actors and directors that appear frequently in the dataset, who is the most worth it? Do these actors and directors consistently appear in one genre or are they profitable across various genres?

# **Question 3** – What movies where the biggest flops? Are there factors that are associated with flops?
#
# **Details** – Given both budget and gross data can you quantify this? Remember the note that some movies may be in different currencies.
