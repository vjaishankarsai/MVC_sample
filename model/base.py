import pymongo

#database connection
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['jai_db']
mycol = mydb["jai_collection"]
