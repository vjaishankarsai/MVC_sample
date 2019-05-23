import request
import response
from flask import request
from model.base import FirstSample

fs = FirstSample()

class UpdationController(object):
    
    def update(self, name, address):
        del_status = fs.update(name,address)
        if del_status == 0:
            return "Unable to Update, the document is not there !!!!!!!!"
        else:
            res = fs.show()
            return res
