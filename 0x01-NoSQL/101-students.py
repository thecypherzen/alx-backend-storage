#!/usr/bin/env python3
"""Defines a function that queries a db"""


def top_students(mongo_collection):
    """Returns all students sorted by average score:

    1. The top must be ordered
    2. The average score must be part of each item returned
       with key = averageScore

    Params:
      mongo_collection(pymongo.Collection): mogodb collection

    Returns: sorted list of students with computed average scores
    """
    return [obj for obj in mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])]
