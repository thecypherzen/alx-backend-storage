# Overview #

## Background Context ##
As RDBMS have increasingly failed to meet the performance, scalability, and flexibility needs that next-generation, data-intensive applications require, NoSQL databases are being rapidcy adopted  by mainstream enterprises as they are usefuld for storing *unstructured data* such as  IoT, device data, videos and images;

In this project, we zoom in on `MongoDB` in order to understand NoSQL databases better. Key concepts convererd include:
- Meaning of NoSQL
- The difference between SQL and NoSQL 
- ACID 
- Types of NoSQL
- Benefits of a NoSQL 
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB


## Reference Materials ##
The following can be used for referencing these areas, curated for optimized understanding:
- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners
](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [Mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)



## Folder Details ###
- **Date Created:** Mon Oct. 21 2024
- **Author:** [William Inyam](https.//github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/0x01-NoSQL).
- **Project Timeline:**
- **Released:** Mon Oct. 21 - 6am.
  - **1st Deadline** Wed Oct. 23 2024 - 6am.
  - **Duration:** 48hrs
  - **Completed:** Tue Oct. 22 2024 - 11:05am.


## Development Environment ##
### Install MongoDB 4.2 in Ubuntu 18.04 ###

``` sh
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -

$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list


$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
# mongod start/running, process 3627


$ mongos --version
# Output
# MongoDB shell version v4.2.8
# git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
# OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
# allocator: tcmalloc
# modules: none
# build environment:
#    distmod: ubuntu1804
#    distarch: x86_64
#    target_arch: x86_64
  
$ pip3 install pymongo

```
[See Official installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

*Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found, terminating:([MacOS](https://bryantson.medium.com/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479), [Linux](https://stackoverflow.com/questions/37702957/mongodb-data-db-not-found))*

``` sh
# try: 
$ sudo mkdir -p /data/db
```

*Or if `/etc/init.d/mongod` is missing, here's example of the [file](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x01-NoSQL/.mongo_script.sh).*<br/>

## Files  ###
*This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|------------------------------|-----------------------------------------------------|
| 1. | [0-list_databases](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x01-NoSQL/0-list_databases) | A script that lists all databases in MongoDB. |
| 2. | [1-use_or_create_database](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x01-NoSQL/0-list_databases) | A script that creates or uses the database `my_db` |
| 3. | [2-insert](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/2-insert) | A script that inserts a document in the collection `school`. The db name is passed as an option to `mongo`/`mongosh` | 
| 4. | [3-all](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/3-all) | A script that lists all documents in the collection `school`. The db name is passed as an option to `mongo`/`mongosh`. | 
| 5. | [4-match](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/4-match) | A script that lists all documents with `name="Holberton school"` in the collection `school`. The db     
      name is passed as an option to `mongo`/`mongosh`. | 
| 6. | [5-count](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/5-count) | A script that displays the number of documents in the collection `school`. The db name is passed as an option to `mongo`/`mongosh`.| 
| 7. | [6-update](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/6-update) | A script that adds a new attribute to a document in the collection `school`. Requirements in file. | 
| 8. | [7-delete](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/7-delete) | A script that deletes all documents with `name="Holberton school"` in collection `school`. The db name is passed as an option to `mongo`/`mongosh`. | 
| 9. | [8-all.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/8-all.py) | A  Python function that lists all documents in a collection. <ul><li><i>Prototype:</i> `def list_all(mongo_collection)`</li></ul>| 
| 10. | [9-insert_school.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/9-insert_school.py) | A Python function that inserts a new document in a collection based on `kwargs`.<ul><li><i>Prototype:</i> `def insert_school(mongo_collection, **kwargs)`</li></ul> | 
| 11. | [10-update_topics.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/10-update_topics.py) | A Python function that changes all topics of a school document based on the name. <ul><li><i>Prototype:</i> `def update_topics(mongo_collection, name, topics)`</li></ul>| 
| 12. | [11-schools_by_topic.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/11-schools_by_topic.py) | A Python function that returns the list of school having a specific topic. <ul><li><i>Prototype:</i> `def schools_by_topic(mongo_collection, topic)`</li></ul>| 
| 13. | [12-log_stats.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/12-log_stats.py) | A Python script that provides some stats about Nginx logs stored in MongoDB. Dummy data [here](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/dump).| 
| 14. | [100-find](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/100-find) | A script that lists all documents with `name` starting with `Holberton` in the collection `school`. | 
| 15. | [101-students.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/101-students.py) | A Python function that returns all students sorted by average score. <ul><li><i>Prototype</i>`def top_students(mongo_collection)`</li></ul>|
| 16. | [102-log_stats.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/102-log_stats.py) | A modification of [12-log_stats.py](https://github.com/thecypherzen/alx-backend-storage/tree/main/0x01-NoSQL/12-log_stats.py), adding the top 10 of the most present IPs in the collection `nginx` of the database  `logs`. |
