#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDb

  Database: logs
  Collection: nginx
  Display using this format:
   - first line: x logs where x is the number of documents in this collection
   - second line: Methods:
   - 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
   - one line with the number of documents with:
      - method=GET
      - path=/status
   - test data in file `dump`
   Example:
   94778 logs
   Methods:
        method GET: 93842
        method POST: 229
        method PUT: 0
        method PATCH: 0
        method DELETE: 0
   47415 status check
"""


from pymongo import MongoClient

client: MongoClient = MongoClient("mongodb://localhost:27017")
nginx = client.logs.nginx
res = f"""{nginx.count({})} logs
Methods:
\tmethod GET: {nginx.count({'method': 'GET'})}
\tmethod POST: {nginx.count({'method': 'POST'})}
\tmethod PUT: {nginx.count({'method': 'PUT'})}
\tmethod PATCH: {nginx.count({'method': 'PATCH'})}
\tmethod DELETE: {nginx.count({'method': 'DELETE'})}
{nginx.count({'$and': [{'method': 'GET'}, {'path': '/status'}]})} status check"""
print(res)
