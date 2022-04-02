from flask import Blueprint
from ms import app


web = Blueprint('web', __name__, url_prefix="/")


@web.route("/")
def index():
    print(app.config.get("APP_VERSION"))
    return "hello from flask"

