"""_summary_

Returns:
    _type_: _description_
"""

import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500
    return f"This page has been seen {page_views} times."


@cache
def redis():
    """_summary_

    Returns:
        _type_: _description_
    """
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
