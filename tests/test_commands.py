import os
from fixture import app, client, runner
from ms.commands import pep8


def test_command_pep8(runner):
    file = "./tests/pep8file.py"

    f = open(file, "w+")
    f.write("""
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)""")
    f.close()

    runner.invoke(pep8, ["--path", file])

    formated = """
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
"""

    assert formated == open(file).read()
    os.remove(file)
