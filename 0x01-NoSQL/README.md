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
  - **Completed:** pending.


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
 
