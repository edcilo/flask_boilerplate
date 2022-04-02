from ms import app


@app.route("/")
def index():
    return "hello from flask"
