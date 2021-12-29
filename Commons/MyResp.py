from flask import make_response, jsonify


def myResp(data):
    resp = make_response(jsonify(data))
    return resp
