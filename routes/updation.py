from flask import Blueprint
from flask import request
from flask import jsonify
from controller.UpdationController import UpdationController

#to create an object for blueprint
bp = Blueprint(__name__, "updation")

#to create an object for updation controller
icc = UpdationController()

@bp.route("/updation", methods=["POST"])
def insertion():
    data = request.get_json()                           #to get data
    name = data["name"]
    address = data["address"]
    update_result = icc.update(name, address)           #call update method in controller
    return jsonify(update_result)                       #to return the result in the json format 
