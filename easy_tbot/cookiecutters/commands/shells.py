from ...shell.custom.backend import ShellCommand
from cookiecutter.main import cookiecutter
from pathlib import Path

class CreateFragment(ShellCommand):
    name = 'createfragment'
    extra = {'help': 'create a fragmment of logic'}

    def do(self):
        p = Path(__file__).parent/'app.zip'
        cookiecutter(str(p))