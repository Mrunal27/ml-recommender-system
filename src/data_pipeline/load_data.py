import os
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = os.path.join(os.path.dirname(__file__),'..','..','data')
BASE_DIR = os.path.abspath(BASE_DIR)

ratings_file = os.path.join(BASE_DIR, 'u.data')
movies_file = os.path.join(BASE_DIR, 'u.item')

ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(ratings_file, sep='\t', names=ratings_cols)

movies_cols= ['movie_id', 'title'] + [f'genre_{i}' for i in range(19)]
movies = pd.read_csv(movies_file, sep='|', names=movies_cols, encoding='latin-1')

ratings.drop('timestamp', axis=1, inplace=True)
movies = movies[['movie_id', 'title']]

db_file = os.path.join(BASE_DIR, 'recommender.db')
engine = create_engine(f'sqlite:///{db_file}', echo=False)
ratings.to_sql('ratings', con=engine, if_exists='replace', index=False)
movies.to_sql('movies', con=engine, if_exists='replace', index=False)

print("Data loaded into SQLite DB Successfully!")