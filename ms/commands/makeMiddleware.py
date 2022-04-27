import click
import os
from flask.cli import with_appcontext


@click.command(name='make:middleware',
               help='Create a new middleware class')
@click.option("-n", "--name", required=True, help="The name of the class")
@with_appcontext
def makemiddleware(name):
    appPath = os.path.realpath("")
    middlewaresPath = "ms/middlewares"
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, middlewaresPath, f"{filename}.py")

    controller = open(fullpath, "w+")
    controller.write(f'''from flask import abort
from .middleware import Middleware


class {name}(Middleware):
    def handler(self, request):
        return True
''')
    controller.close()
