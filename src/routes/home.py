from flask import Blueprint

_home = Blueprint("home", __name__)


@_home.route("/", methods=["GET"])
def home():
    return {"message": "Welcome to the flask template"}, 200
