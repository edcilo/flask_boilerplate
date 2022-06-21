import click
import os
import re
from flask.cli import with_appcontext


@click.command(name='make:repository',
               help='Create a new repository class')
@click.option('-n', '--name', required=True, help='The name of the class')
@with_appcontext
def makerepository(name):
    appPath = os.path.realpath('')
    modelsPath = 'ms/repositories'
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, modelsPath, f"{filename}.py")

    model = open(fullpath, 'w+')
    model.write(f'''from .repository import Repository


class {name}(Repository):
    def get_model(self):
        pass
''')
    model.close()
