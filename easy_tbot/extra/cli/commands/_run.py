from easy_tbot.core.cli.decorator import command
from easy_tbot.core.client import loader


@command
def run():
    loader().run()
