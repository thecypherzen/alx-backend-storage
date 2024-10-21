#!/usr/bin/env python3
"""A function that Insert a document in Python"""


def insert_school(mongo_collection, **kwargs) -> str:
    """Inserts a new document in a collection from <kwargs>

    Params:
        mongo_collection(class:pymongo.Collection): a collection object
        kwargs(dict): keword argument object

    Returns:
        Id of newly added document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
