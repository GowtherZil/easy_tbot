"""This module hold the migrate command"""
# We import module decorator to make commands
from easy_tbot.core.cli.decorator import command

# and the main backend loader called [DataBase](ref:easy_tbot.core.bot.loader:DataBase)  that hold 
# the [SqlAlchemyBackend](ref:easy_tbot.contrib.db.backend:SqlAlchemyBackend))
# in this case
from easy_tbot.core.db import loader


# ## The super simple migrate command
@command
def migrate():
    loader().migrate()
