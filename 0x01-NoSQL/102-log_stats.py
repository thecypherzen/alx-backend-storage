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
    from pymongo import MongoClient

    client: MongoClient = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # calculate and log out methods data
    print(f"{nginx.count({})} logs\nMethods:")
    for method in methods:
        print(f"\t{method}: {nginx.count({'method': method})}")

    # log out status data
    print(f"""{nginx.count({
    '$and': [{'method': 'GET'},
    {'path': '/status'}]})} status check""")

    # aggregate ip count data
    ip_counts = nginx.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # log out ips data
    print("IPs:")
    for ip_count in ip_counts:
        print(f"\t{ip_count['_id']}: {ip_count['count']}")
