import request
import response
from flask import request
from model.base import FirstSample

fs = FirstSample()

class DeletionController(object):
    
    def remove(self, name):
        del_status = fs.remove(name)
        if del_status == 0:
            return "Sorry no such document is present!!!!!!!!!"
        else:
            res = fs.show()
            return res
