import request
import response
from flask import request
from model.base import FirstSample

fs = FirstSample()

class InsertionController(object):
    
    def insert(self, name, address):
        ins_status = fs.add(name,address)
        if ins_status == 0:
            return "Duplicate name found, please give another name"
        else:
            res = fs.show()
            return res
