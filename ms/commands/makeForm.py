import click
import os
from flask.cli import with_appcontext


@click.command(name='make:form',
               help='Create a new form class')
@click.option("-n", "--name", required=True, help="The name of the form")
@with_appcontext
def makeform(name):
    appPath = os.path.realpath("")
    formsPath = "ms/forms"
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, formsPath, f"{filename}.py")

    form = open(fullpath, "w+")
    form.write(f'''from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Required


class {name}(FormRequest):
    def rules(self):
        return {{}}
''')
    form.close()
