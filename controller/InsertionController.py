from model import mycol
from . import Common

c=Common.Common()

class InsertionController(object):
    
    #method to insert the document
    def insert(self, name, address):
        if(not (c.find_doc(name))):                                     #search the db for that document using 'name', if it is not present
            mdict = { "_id": name, "address": address }                 #add name and address to a dictionary
            mycol.insert_one(mdict)                                     #insert into the db
            return c.show()                                             #to return all the documents in the database
        else:
            return "Duplicate name found, please give another name"     #If document is present then return that msg
