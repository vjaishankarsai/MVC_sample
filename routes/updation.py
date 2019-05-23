from flask import Blueprint
from flask import request
from flask import jsonify
from controller.UpdationController import UpdationController


bp = Blueprint(__name__, "updation")

icc = UpdationController()

@bp.route("/updation", methods=["POST"])
def insertion():
    data = request.get_json()
    name = data["name"]
    address = data["address"]
    update_result = icc.update(name, address)
    return jsonify(update_result)
