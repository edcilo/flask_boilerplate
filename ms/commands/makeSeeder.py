import click
import os
import re
from flask.cli import with_appcontext


@click.command(name='make:seeder',
               help='Create a new seeder class')
@click.option('-n', '--name', required=True, help='The name of the seeder')
@with_appcontext
def makeseeder(name):
    appPath = os.path.realpath('')
    seederPath = 'ms/db/seeders'
    filename = f"{name[0].lower()}{name[1:]}"
    fullpath = os.path.join(appPath, seederPath, f"{filename}.py")

    seeder = open(fullpath, 'w+')
    seeder.write(f'''from faker import Faker
from flask_seeder import Seeder, generator


class {name}(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        fake = Faker()
''')
    seeder.close()
