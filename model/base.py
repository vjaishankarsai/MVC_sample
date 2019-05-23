import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['jai_db']
mycol = mydb["jai_collection"]

class FirstSample:

    def add(self, name, address):
        if mycol.count_documents({'_id': name}) <= 0 :
            mdict = { "_id": name, "address": address }
            mycol.insert_one(mdict)
            return 1
        else:
            return 0
    def show(self):
        List = []
        for i in mycol.find():
            List.append(i)
        return List
    
    def remove(self,name):
        if mycol.count_documents({'_id': name}) > 0 :
            myquery = { "_id" : name}
            mycol.delete_one(myquery)
            return 1
        else: 
            return 0
        
    def update(self, name, newaddress):
        if mycol.count_documents({'_id': name}) > 0 :
            myquery = { "_id" : name }
            newvalues = { "$set" : { "address" : newaddress } }
            mycol.update_one(myquery,newvalues)
            return 1
        else:
            return 0
