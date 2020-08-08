import http
from flask import Blueprint

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blueprint.route("/", methods=["GET"])
@admin_blueprint.route("/index", methods=["GET"])
def index():
    return "Forbidden", http.HTTPStatus.FORBIDDEN
