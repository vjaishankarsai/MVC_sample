from flask import Blueprint
from flask import request
from flask import jsonify
from controller.DeletionController import DeletionController


bp = Blueprint(__name__, "deletion")

icc = DeletionController()

@bp.route("/deletion", methods=["POST"])
def deletion():
    data = request.get_json()
    name = data["name"]
    del_result = icc.remove(name)
    return jsonify(del_result)
