# 🎬 Movie Recommender System

A simple baseline recommender system using Python, Pandas, and FastAPI. The project loads movies/ratings from a SQLite database and serves top-N recommendations through an API.

---

## 🚀 Features

* Load and preprocess movies/ratings dataset from SQLite
* Compute average rating per movie (baseline recommender)
* Serve API endpoints using **FastAPI + Uvicorn**
* Easily extensible for collaborative filtering, content-based, or ML-driven models

---

## 📂 Project Structure

```
ml-recommender-system/
│── data/                 # Database + raw datasets (ignored by git)
│   └── recommender.db
│── src/
│   ├── api/
│   │   └── main.py       # FastAPI server
│   └── models/
│       └── baseline.py   # Baseline recommender logic
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<your-username>/ml-recommender-system.git
cd ml-recommender-system
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate environment

* On **Windows (PowerShell)**

  ```bash
  venv\Scripts\activate
  ```
* On **macOS/Linux**

  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Add dataset

* Place your SQLite database inside the `data/` folder.
* Example file:

  ```
  data/recommender.db
  ```

  The DB should contain at least two tables:

  * **movies** → `movie_id`, `title`
  * **ratings** → `user_id`, `movie_id`, `rating`

### 6️⃣ Run FastAPI server

```bash
uvicorn src.api.main:app --reload
```

Server will start at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📡 API Endpoints

* **Get top-N movies**

  ```
  GET /recommendations?top_n=5
  ```

  Example Response:

  ```json
  [
    {"movie_id": 1, "title": "Toy Story", "rating": 4.3},
    {"movie_id": 2, "title": "The Matrix", "rating": 4.2},
    ...
  ]
  ```

---

## 🛠️ Next Steps

* Add collaborative filtering model
* Add content-based filtering using metadata (genres, tags)
* Deploy on cloud (Heroku, AWS, etc.)



