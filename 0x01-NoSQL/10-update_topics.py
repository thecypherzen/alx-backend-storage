#!/usr/bin/env python3
"""Defines a function to change school topics"""


def update_topics(mongo_collection, name, topics) -> None:
    """Changes all topics of a school document based on the name

    Params:
       mongo_collection(pymongo.Collection): mongodb collection object
       name(str): the school name to update
       topids(list[str]): list of topics offered in the school

    Returns:
       None
    """
    mongo_collection.update(
        {"name": name}, {"$set": {"topics": topics}}
    )
