import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
dblist = myclient.list_database_names()
mycol = mydb
