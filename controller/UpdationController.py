from model import mycol
from . import Common

c=Common.Common()

class UpdationController(object):
    
    #method to remove the document
    def update(self, name, newaddress):
        if(c.find_doc(name)):                                                 #search the db for that document using 'name'  
            myquery = { "_id" : name }                                        
            newvalues = { "$set" : { "address" : newaddress } }
            mycol.update_one(myquery,newvalues)                               #to update the document
            return c.show()                                                   #to return all the documents in the database
        else:
            return "Unable to Update, the document is not there !!!!!!!!"     #If document is not present then return that msg
