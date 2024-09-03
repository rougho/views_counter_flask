from redis import Redis
from flask import Flask


app = Flask(__name__)
redis = Redis()

@app.get("/")
def index():
    page_views = redis.incr("page_view")
    return f"This page has been seen {page_views} times."

