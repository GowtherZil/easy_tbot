"""This module contains a database backend based on sqlalchemy"""
try:
    import sqlalchemy
    # assert sqlalchemy.__version__ >= 1.4
except:
    print("Warning: Code in `easy_tbot.contrib.db.alchemy` requires `sqlalchemy>=1.4`.")
    print("FIX: You can install it with `pip install easy_tbot[sql]`.")
    raise

from ._backend import SqlAlchemyBackend
from ._shorcuts import model, session, session_scope