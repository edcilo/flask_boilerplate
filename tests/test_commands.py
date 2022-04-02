import os
from fixture import app, client, runner
from ms.commands import pep8, makecontroller, makemiddleware


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


def test_command_makecontroller(runner):
    nameController = "mockController"
    appPath = os.path.realpath("")
    controllerPath = "ms/controllers"
    fullPath = os.path.join(appPath, controllerPath, f"{nameController}.py")

    runner.invoke(makecontroller, ['--name', nameController])

    assert os.path.exists(fullPath)
    os.remove(fullPath)



def test_command_makemiddleware(runner):
    nameController = "mockMiddleware"
    appPath = os.path.realpath("")
    controllerPath = "ms/middlewares"
    fullPath = os.path.join(appPath, controllerPath, f"{nameController}.py")

    runner.invoke(makemiddleware, ['--name', nameController])

    assert os.path.exists(fullPath)
    os.remove(fullPath)
