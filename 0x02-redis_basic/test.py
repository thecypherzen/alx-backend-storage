#!/usr/bin/env python3


from uuid import uuid4
# from exercise import Cache
from functools import wraps
from redis import Redis
from inspect import signature


redis = Redis.from_url("redis://localhost:6379/1")
# cache  = Cache()

def expose(func):
    # @wraps(func)
    def wrapper(*args):
        print("FIRST ARGUMENT: ", args[0])
        func(*args)
    return wrapper


@expose
def myfunc(string):
    print(myfunc.__name__, "just executed")



print(myfunc.__globals__)
