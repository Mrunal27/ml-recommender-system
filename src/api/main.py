from fastapi import FastAPI
from src.models.baseline import get_top_movies

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "ML Recommender Sytem API is running!"}


@app.get("/recommend/{user_id}")
def recommend(user_id: int, top_n: int=10):
    top_movies = get_top_movies(top_n)
    return {"user_id": user_id, "recommendations": top_movies}