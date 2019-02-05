import requests
import time
import re

import pandas as pd
from bs4 import BeautifulSoup


def scrape_eberts_listing(num_pages=10):
    """
    Parses through webpage with list of movies and returns DataFrame.
    :num_pages = Number of pages to go through
    """
    url = "http://www.rogerebert.com/reviews?great_movies=0&no_stars=0&title=Cabin+in+the+Woods&filtersgreat_movies%5D%5B%5D=&filters%5Bno_stars%5D%5B%5D=&filters%5Bno_stars%5D%5B%5D=1&filters%5Btitle%5D=&filters%5Breviewers%5D=&filters%5Bgenres%5D=&page={}&sort%5Border%5D=newest"
    pages = list(range(1, num_pages))
    links = [url.format(i) for i in pages]

    review_list = list()
    count = 0

    for link in links:
        webpage = requests.get(link).text
        soup = BeautifulSoup(webpage, 'lxml')
        all_movies = soup('figure', {'class':'movie review'})

        for movie in all_movies:
            url = movie.a.get('href')
            title = movie.find_all('a')[1].text
            stars = len(movie.find_all('i', {'class':'icon-star-full'})) + 0.5 * len(movie.find_all('i', {'class':'icon-star-half'}))

            try:
                year = movie.find('span', {'class':'release-year'}).text[1:-1]
            except:
                year = ''

            count += 1
            review_list.append([count, title, stars, year, url])


    df = pd.DataFrame(review_list, columns = ['id', 'title', 'ebertstars', 'year', 'url'])
    return df

def scrape_movie_reviews(df):
    """
    Parses each individual review page and returns list of key attributes.
    :link = URL for review
    """
    scraped_list = list()

    for link in df['url']:
        full_link = "http://www.rogerebert.com" + link
        webpage = requests.get(full_link).text
        soup = BeautifulSoup(webpage, 'lxml')

        try:
            mpaa = soup.find('p', {'class':'mpaa-rating'}).strong.text[6:]
        except:
            mpaa = ''

        try:
            runtime = int(soup.find('p', {'class':'running-time'}).strong.text[:3].strip())
        except:
            runtime = ''

        try:
            review = ' '.join([paragraph.text for paragraph in soup.find('div', {'itemprop':'reviewBody'}).find_all('p')])
        except:
            review = ''

        scraped_list.append([link, mpaa, runtime, review])

        time.sleep(0.25)

    df = pd.DataFrame(scraped_list, columns = ['url', 'rating', 'runtime', 'review'])

    return df, scraped_list

def scrape_imdb_listing(df):
    """
    Searches IMDB, parses results and returns DataFrame.
    :df = DataFrame with movie titles
    """
    movie_list = list()

    for movie in df['title']:
        base_url = 'http://www.imdb.com/find?q='
        url = base_url + movie +'&s=all'
        webpage = requests.get(url).text
        soup = BeautifulSoup(webpage, 'lxml')

        try:
            results = soup('table', {'class':'findList'})[0]
        except:
            continue

        title = results.find_all('tr')[0]
        link = title.find('a', href=True)['href']

        url = 'http://www.imdb.com' + link
        webpage = requests.get(url).text
        soup = BeautifulSoup(webpage, 'lxml')

        movie_title = soup.find('title')

        try:
            rate = soup.find('span', itemprop='ratingValue').text
        except:
            rate = ''

        try:
            count = soup.find('span', itemprop='ratingCount').text
        except:
            count = ''

        try:
            des = soup.find('meta',{'name':'description'})['content']
        except:
            des = ''

        try:
            metascore = soup.find('div', class_='metacriticScore').text
        except:
            metascore = ''

        try:
            reviews_count = soup.find('div', class_='titleReviewbarItemBorder')
            u_reviews = reviews_count.find_all('a')[0].text.split(' ')[0]
            c_reviews = reviews_count.find_all('a')[1].text.split(' ')[0]
        except:
            u_reviews = ''
            c_review = ''

        try:
            director = soup.find('span', itemprop='name').text
        except:
            director = ''

        try:
            country = soup.find('div', class_='subtext').find_all('a', title=True)[-1].text.split(' ')[-1]
            country = re.sub('[\(\)\{\}<>]', '', country)
        except:
            country = ''

        try:
            rel_date = (', ').join(soup.find('div', class_='subtext').find_all('a',
                                            title=True)[-1].text.split(' ')[:-1])
        except:
            rel_date = ''

        movie_list.append([movie, rate, count, des, metascore, u_reviews, c_reviews,
                       director, country, rel_date])

        time.sleep(0.25)


    df = pd.DataFrame(movie_list, columns = ['title', 'imdb_rating', 'rating_count',
        'description', 'metascore', 'user_review_count', 'critic_review_count',
        'director', 'country', 'release_date'])

    return df, movie_list
