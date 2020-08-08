import http
from flask import Blueprint

root_blueprint = Blueprint("root", __name__, url_prefix="/")


@root_blueprint.route("/", methods=["GET"])
@root_blueprint.route("/index", methods=["GET"])
def index():
    return "Hello, World!", http.HTTPStatus.OK
