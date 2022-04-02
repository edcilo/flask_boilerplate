from ms import app
from .autopep8 import pep8


app.cli.add_command(pep8)
