from functools import cache
from redis import Redis
from flask import Flask


app = Flask(__name__)

@app.get("/")
def index():
    page_views = redis().incr("page_views")
    return f"This page has been seen {page_views} times."

@cache
def redis():
    return Redis()