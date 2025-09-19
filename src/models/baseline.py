import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

# --- Load ratings ---
ratings_file = os.path.join(BASE_DIR, 'u.data')
ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(ratings_file, sep='\t', names=ratings_cols)
ratings['movie_id'] = ratings['movie_id'].astype(int)

# --- Load movies ---
movies_file = os.path.join(BASE_DIR, 'u.item')
movies = pd.read_csv(
    movies_file,
    sep='|',
    encoding='latin-1',
    usecols=[0, 1],
    names=['movie_id', 'title'],
    header=None
)
movies['movie_id'] = movies['movie_id'].astype(int)

# --- Compute average rating per movie ---
movie_stats = ratings.groupby('movie_id')['rating'].mean().reset_index()
movie_stats = movie_stats.merge(movies, on='movie_id', how='inner')

# --- Get top N movies ---
def get_top_movies(n=10):
    top_movies = movie_stats.sort_values('rating', ascending=False).head(n)
    return top_movies[['movie_id', 'title', 'rating']].to_dict(orient='records')

if __name__ == "__main__":
    top = get_top_movies()
    for i, movie in enumerate(top, 1):
        print(f"{i}. {movie['title']} ({movie['rating']:.2f})")
