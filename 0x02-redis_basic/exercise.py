#!/usr/bin/env python3
"""Creates the class `Cache`"""
from redis import Redis
from typing import Callable, Optional, Union
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

    def get(self, key: str,
            fn: Optional[Callable[
                [bytes], Union[str, bytes, int, float]
            ]] = None) -> Union[str, bytes, int, float, None]:
        """Fetches a value from the database and converts to
        the correct type using <fn>
        Params:
           key(str): key of the item in db
           fn(obj:callable): functino to use for conversion
        """
        if not key or not (data := self._redis.get(key)):
            None
        if not fn:
            return data
        return fn(data)

    def get_int(self, key: str) -> Union[int, None]:
        """Converts a value of key to type int"""
        if not key:
            return None
        data: bytes = self.__redis.get(key)
        if not data:
            return None
        return self.get(key, int.from_bytes)

    def get_str(self, key: str) -> Union[str, None]:
        """Converts value of a key to type str"""
        if not key:
            return None
        data: bytes = self.__redis.get(key)
        if not data:
            return None
        return self.get(key, lambda val: val.decode("utf-8"))

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the input data
        in Redis using the random key and returns the key.
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
