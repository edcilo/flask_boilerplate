import click
import os
import re
from flask.cli import with_appcontext


@click.command(name='make:serializer',
               help='Create a new serializer class')
@click.option('-n', '--name', required=True, help='The name of the serializer')
@with_appcontext
def makeserializer(name):
    appPath = os.path.realpath('')
    serializerPath = 'ms/serializers'
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, serializerPath, f"{filename}.py")

    seeder = open(fullpath, 'w+')
    seeder.write(f'''from ms.serializers import Serializer


class {name}(Serializer):
    response = {{
        "id": str,
    }}
''')
    seeder.close()
