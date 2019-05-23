from flask import Blueprint
from flask import request
from flask import jsonify
from controller.InsertionController import InsertionController


bp = Blueprint(__name__, "insertion")

icc = InsertionController()

@bp.route("/insertion", methods=["POST"])
def insertion():
    data = request.get_json()
    name = data["name"]
    address = data["address"]
    ins_result = icc.insert(name, address)
    return jsonify(ins_result)
