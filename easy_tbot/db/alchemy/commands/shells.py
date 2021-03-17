from ....shell.custom.backend import ShellCommand
from ...loader import DataBase
class MigrateShellCommand(ShellCommand):
    """
    Command that migrates all models in the database
    """
    name = 'migrate'
    extra = {
        'help': 'Populate the data base with models'
    }

    def do(self, *args, **kwargs):
        db  = DataBase()
        db.migrate()

    def post_insert(self, parser):
        pass