#!/usr/bin/env python3
"""Creates the class `Cache`"""
from redis import Redis
from typing import Union
from uuid import uuid4


class Cache:
    """Represents a Cache
    Attributes:
       _redis(obj:redis): instance of the redis client.
    Methods:
        store(data) -> string: Generates a random key
    """
    def __init__(self):
        """Initializes instance of `Cache`"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the input data
        in Redis using the random key and returns the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
