#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDb

  Database: logs
  Collection: nginx
  Display using this format:
   - first line: x logs where x is the number of documents in this collection
   - second line: Methods:
   - 5 lines with the number of documents with the
     method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this
     order (see example below - warning: it’s a tabulation
     before each line)
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

if __name__ == "__main__":
    from collections import Counter
    from pymongo import MongoClient

    client: MongoClient = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx
    result = ""
    # get ips from db and group by count
    ip_docs = nginx.find({}, {"ip": 1})
    ip_counter = Counter(list(doc['ip'] for doc in ip_docs))
    top_ten = ip_counter.most_common(10)
    for top_ip in top_ten:
        result += f"\t{top_ip[0]}: {top_ip[1]}\n"

    res = f"""{nginx.count({})} logs
Methods:
\tmethod GET: {nginx.count({'method': 'GET'})}
\tmethod POST: {nginx.count({'method': 'POST'})}
\tmethod PUT: {nginx.count({'method': 'PUT'})}
\tmethod PATCH: {nginx.count({'method': 'PATCH'})}
\tmethod DELETE: {nginx.count({'method': 'DELETE'})}
{nginx.count({'$and': [{'method': 'GET'},
{'path': '/status'}]})} status check
IPS:
{result}"""
    print(res, end="")
