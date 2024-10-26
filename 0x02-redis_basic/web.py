#!/usr/bin/env python3
import functools
import requests
import redis


cache = redis.Redis()
cache.flushdb()


def track_count(func):
    """tracks how often a url is visited"""
    @functools.wraps(func)
    def wrapper(url):
        key = f"count:{url}"
        cache.incr(key)
        res = cache.get(func.__qualname__)
        if res:
            return str(res, "utf-8")
        res = func(url)
        res_text = res.text
        cache.setex(f"{func.__qualname__}", 10, res_text)
        return res_text
    return wrapper


@track_count
def get_page(url: str) -> str:
    """Uses the requests module to obtain the HTML content of a
    particular URL and returns it
    Tracks how many times a particular URL was accessed in the
    key "count:{url}" and caches the result with an expiration
    time of 10 seconds.
    """
    response = requests.get(url)
    return response.text
