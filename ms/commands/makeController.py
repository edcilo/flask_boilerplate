import click
import os
from flask.cli import with_appcontext


@click.command(name='make:controller',
               help='Create a new controller class')
@click.option("-n", "--name", required=True, help="The name of the class")
@with_appcontext
def makecontroller(name):
    appPath = os.path.realpath("")
    controllersPath = "ms/controllers"
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, controllersPath, f"{filename}.py")

    controller = open(fullpath, "w+")
    controller.write(f'''from flask import jsonify
from ms import app
from .controller import Controller


class {name}(Controller):
    def index(self):
        response = {{"foo": "bar"}}
        return jsonify(response), 200
''')
    controller.close()
