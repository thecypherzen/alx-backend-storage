#!/usr/bin/env python3
"""A function that filtrs collection documents by a criteria"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of schools that have a specific topic

    Params:
       mongo_collection(pymongo.Collection): a pymongo collection object
       topic(str): the topic to filter by
    """
    return [obj for obj in mongo_collection.find({"topics": topic})]
