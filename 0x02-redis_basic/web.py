#!/usr/bin/env python3
"""Defines a function to track requests to various urls"""
from typing import Callable
import functools
import requests
import redis


cache = redis.Redis()


def track_count(func: Callable) -> Callable:
    """tracks how often a url is visited"""
    @functools.wraps(func)
    def wrapper(url: str) -> str:
        cache.incr(f"count:{url}")
        count = cache.get(f"count:{url}")
        res = cache.get(f"{url}")
        if res:
            res = str(res, "utf-8")
            return res
        res = func(url)
        cache.setex(f"{url}", 10, res)
        return res
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
