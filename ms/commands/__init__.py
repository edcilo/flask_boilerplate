from ms import app
from .autopep8 import pep8
from .makeController import makecontroller
from .makeMiddleware import makemiddleware
from .makeModel import makeModel
from .makeSeeder import makeSeeder


app.cli.add_command(pep8)
app.cli.add_command(makecontroller)
app.cli.add_command(makemiddleware)
app.cli.add_command(makeModel)
app.cli.add_command(makeSeeder)
