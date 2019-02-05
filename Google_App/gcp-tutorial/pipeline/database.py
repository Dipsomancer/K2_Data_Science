from sqlalchemy import create_engine

def insert_db(df, name, engine):
    df.to_sql(name, engine, if_exists="replace")

    return None
