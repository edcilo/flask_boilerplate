import click
import os
import re
from flask.cli import with_appcontext


@click.command(name='make:model',
               help='Create a new model class')
@click.option('-n', '--name', required=True, help='The name of the class')
@with_appcontext
def makemodel(name):
    appPath = os.path.realpath('')
    modelsPath = 'ms/models'
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, modelsPath, f"{filename}.py")
    tableName = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    model = open(fullpath, 'w+')
    model.write(f'''import datetime
import uuid
from ms.db import db


class {name}(db.Model):
    __tablename__ = '{tableName}'

    _fillable = []

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    def __init__(self, data=None):
        if not data is None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<{name} {{self.id}}>"
''')
    model.close()
