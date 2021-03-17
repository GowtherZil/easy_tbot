from ...shell.custom.backend import ShellCommand
from ..loader import Bot

class RunShellCommand(ShellCommand):
    """
    Command that starts the bot
    """
    name = 'run'
    extra = {
        'help': 'Run bot'
    }

    def do(self, *args, **kwargs):
        bot = Bot()
        bot.run(*args, **kwargs)

    def post_insert(self, parser):
        pass
