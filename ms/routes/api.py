from flask import jsonify, Blueprint
from ms import app


api = Blueprint('api', __name__, url_prefix="/api/v1")


@api.route("/")
def api_index():
    return jsonify({
        "app_name": app.config.get("APP_NAME"),
        "version": app.config.get("APP_VERSION")
    }), 200
