from flask import Blueprint
from ms.controllers import ApiController


api = Blueprint('api', __name__, url_prefix="/api/v1")


@api.route("/")
def api_index():
    return ApiController.action('index')
