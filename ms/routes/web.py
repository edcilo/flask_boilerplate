from flask import Blueprint
from ms.controllers import WebController


web = Blueprint('web', __name__, url_prefix="/")


@web.route("/")
def index():
    return WebController.action('index')
