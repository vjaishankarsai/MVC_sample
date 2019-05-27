from model import mycol

class Common:

    #method to find the document in the database
    def find_doc(self,name):
        if mycol.count_documents({'_id': name}) > 0 :
            return 1                                                #if the document is present return 1
        else:
            return 0                                                # else return 0
    
    #method to fetch all documents in the database
    def show(self):
        List = []
        for i in mycol.find():                                      #fetch all the documents in the db
            List.append(i)                                          #Store the documents in a list
        return List
