#!/usr/bin/env python3
"""List all documents in a mongoDB from Python"""


def list_all(mongo_collection):
    """Lists all documents in a collection
    Params:
      mongo_collection(obj:pymongo.Collection): a collection object
    Returns:
      List of documents in mongo_collection
    """
    return [obj for obj in mongo_collection.find()]
