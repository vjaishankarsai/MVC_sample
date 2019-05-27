from flask import Blueprint
from flask import request
from flask import jsonify
from controller.InsertionController import InsertionController

#to create an object for blueprint
bp = Blueprint(__name__, "insertion")

#to create an object for insertion controller
icc = InsertionController()

@bp.route("/insertion", methods=["POST"])
def insertion():
    data = request.get_json()                           #to get data
    name = data["name"]
    address = data["address"]
    ins_result = icc.insert(name, address)              #call insert method in controller
    return jsonify(ins_result)                          #to return the result in the json format 
