from model import mycol
from . import Common

c=Common.Common()

class DeletionController(object):
    
    #method to remove the document
    def remove(self, name):
        if(c.find_doc(name)):                                           #search the db for that document using 'name'
            myquery = { "_id" : name}                                   
            mycol.delete_one(myquery)                                   #to delete the document
            return c.show()                                             #to return all the documents in the database
        else:
            return "Sorry no such document is present!!!!!!!!!"         #If document is not present then return the msg.  
