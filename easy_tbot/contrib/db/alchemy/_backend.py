"""This module contains the database backend implementation based on sqlalchemy"""

# We import **inspect** for some instrspection or reflectino analisys
import inspect

# and now the objects from sqlalchemy base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

# We import *import_module* method for dynamic importing
from importlib import import_module

# The **cache_property** allow us to simulate lazy evaluation
from functools import cached_property

# Now we import our[ datbase backend](ref:easy_tbot.core.db.backend:Backend) prototype
from easy_tbot.core.db.backend import Backend

# and our settings
from easy_tbot.core.tools.settings import Settings

# To build the class

# ## The sqlalchemy backend
# This is just for sqlalchemy initialization, is like an adapter pattern
class SqlAlchemyBackend(Backend):
    def __init__(self, url):
        self.__engine = create_engine(url)

    @property
    def engine(self):
        return self.__engine

    @cached_property
    def model(self):
        return declarative_base()

    @cached_property
    def session(self):
        return sessionmaker(self.engine.load())

    def migrate(self):
        """
        A helper function that write the proper tables in the database and for some kinds of
        databases (ie sqlite) it generates a database file.
        :return: All subscriptions models of the database, the datatables in raw format.
        """
        subscriptions = []

        def __shard_up(shard):
            app_module = import_module(f"{shard}.models")
            for name, value in inspect.getmembers(app_module, inspect.isclass):
                if (
                    issubclass(value, self.model)
                    and name is not self.model
                    and value.__table__ not in subscriptions
                ):
                    subscriptions.append(value.__table__)

        Settings().setup_shards(__shard_up)
        self.model.metadata.create_all(self.engine, tables=subscriptions)
        return subscriptions
