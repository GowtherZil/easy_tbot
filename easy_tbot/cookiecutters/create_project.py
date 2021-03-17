from cookiecutter.main import cookiecutter
from pathlib import Path

def create():
    file = Path(__file__).parent / 'project.zip'
    cookiecutter(str(file))
