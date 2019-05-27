from flask import Blueprint
from flask import request
from flask import jsonify
from controller.DeletionController import DeletionController

#to create an object for blueprint
bp = Blueprint(__name__, "deletion")

#to create an object for deletion controller
icc = DeletionController()

@bp.route("/deletion", methods=["POST"])
def deletion():
    data = request.get_json()                   #to get data                   
    name = data["name"] 
    del_result = icc.remove(name)               #call remove method in controller
    return jsonify(del_result)                  #to return the result in the json format    
