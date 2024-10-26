#!/usr/bin/env python3
"""Creates the class `Cache`"""
import redis
import functools
from typing import Any, Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Counts every new call to store method"""
    @functools.wraps(method)
    def wrapper(self, data):
        self._redis.incr(method.__qualname__)
        return method(self, data)
    return wrapper


def call_history(method: Callable) -> Callable:
    """A decorator to store the history of inputs and outputs
    for a particular function.
    Everytime the original function will be called, we will add
    its input parameters to one list in redis, and store its
    output into another list.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Modifiies the behaviour of method"""
        in_list = f"{method.__qualname__}:inputs"
        out_list = f"{method.__qualname__}:outputs"

        self._redis.rpush(in_list, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(out_list, res)
        return res
    return wrapper


class Cache:
    """Represents a Cache
    Attributes:
       _redis(obj:redis): instance of the redis client.
    Methods:
        store(data) -> string: Generates a random key
    """
    def __init__(self):
        """Initializes instance of `Cache`"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str,
            fn: Optional[
                Callable[[bytes], Union[str, int, float, bytes]]
                ] = None) -> Union[str, bytes, int, float, None]:
        """Fetches a value from the database and converts to
        the correct type using <fn>
        Params:
           key(str): key of the item in db
           fn(obj:callable): functino to use for conversion
        """
        if not key:
            return None
        data = self._redis.get(key)
        if not data:
            return None
        if not fn:
            return data
        return fn(data)

    def get_int(self, key: str) -> Union[int, str, float, bytes, None]:
        """Converts a value of key to type int"""
        if not key:
            return None
        return self.get(key, fn=lambda n: int(n))

    def get_str(self, key: str) -> Union[int, str, float, bytes, None]:
        """Converts value of a key to type str"""
        if not key:
            return None
        data: bytes = self._redis.get(key)
        if not data:
            return None
        return self.get(key, fn=lambda val: val.decode("utf-8"))

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the input data
        in Redis using the random key and returns the key.
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key


def replay(method):
    """Displays the history of calls of a particular function
    using keys from <call_history>
    """
    in_list = f"{method.__qualname__}:inputs"
    out_list = f"{method.__qualname__}:outputs"

    db = getattr(method.__self__, "_redis")
    inputs = db.lrange(in_list, 0, -1)
    outputs = db.lrange(out_list, 0, -1)
    results = zip(inputs, outputs)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for item in results:
        print(f"{method.__qualname__}(*{str(item[0], 'utf-8')}) ->",
              f"{str(item[1], 'utf-8')}")
