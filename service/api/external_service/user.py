import flask
import requests
from flask import request


def groups_user(user_id, params=None):
    req = requests.Request(method="GET", url=f"http://127.0.0.1:5000/api/user/{user_id}/group",
                           headers=request.headers, params=params)
    with requests.Session() as session:
        r = session.send(req.prepare())
    if params:
        return r.json()
    return flask.jsonify(r.json())


def groups_user_followed(user_id, params=None):
    req = requests.Request(method="GET", url=f"http://127.0.0.1:5000/api/user/{user_id}/group/followed",
                           headers=request.headers, params=params)
    with requests.Session() as session:
        r = session.send(req.prepare())
    return flask.jsonify(r.json())
