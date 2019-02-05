from sqlalchemy import create_engine

from ingestion import scrape_eberts_listing, scrape_movie_reviews, scrape_imdb_listing
from storage import archive_data
from processing import clean_ebert_listings, clean_ebert_reviews, clean_imdb
from database import insert_db

if __name__ == "__main__":
    print("This pipeline scrapes, cleans and stores movie data from Roger Ebert and IMDB's website.")

    # Initialize database connection
    try:
        engine = create_engine('postgresql://postgres:password@35.192.138.21:5432/postgres')
        print("Database found.")
    except:
        print("No database available.")
        quit()

    # Ebert's website for listings
    pages = int(input("How many pages would you like to scrape (24 movies per page)? "))
    print("Scraping movie listings from Ebert's website.")
    ebert_listing = scrape_eberts_listing()
    archive_data(ebert_listing, "ebert_listing")
    ebert_listing = clean_ebert_listings(ebert_listing)
    insert_db(ebert_listing, 'ebert_listing', engine)

    # Ebert's website for reviews
    print("Scraping movie reviews from Ebert's website.")
    ebert_reviews, _ = scrape_movie_reviews(ebert_listing)
    archive_data(ebert_reviews, "ebert_reviews")
    ebert_reviews = clean_ebert_reviews(ebert_reviews)
    insert_db(ebert_reviews, 'ebert_reviews', engine)

    # IMDB website for other movie info
    print("Scraping movie information from IMDB.")
    imdb_info, _ = scrape_imdb_listing(ebert_listing)
    archive_data(imdb_info, "imdb_info")
    imdb_info = clean_imdb(imdb_info)
    insert_db(imdb_info, 'imdb_info', engine)

    print("Program complete.")
