"""This module contains a set of shortcuts based on sqlalchemy ORM"""

# We import firts the main backend. The main backend hold 
# the [SqlAlchemyBackend](ref:easy_tbot.contrib.db.backend:SqlAlchemyBackend))
# in this case
from easy_tbot.core.db import loader
# and the **SQLAlchemySession** for some anotation and static typing
from sqlalchemy.orm import Session as SQlAlchemySession
# We import the **contextmanager** method becouse one of our shortcuts
# work like a python context manager
from contextlib import contextmanager


# We create a model variable for further use. The models of our bots need to inherit from it
def model():
    return loader().model

# and we do the same with sessions to create a shortcut
def session():
    return loader().session()

# But we can go a little further using a context manager. 
@contextmanager
def session_scope() -> SQlAlchemySession:
    """
    A context for sections, for properly management of our section.
    Example: with session_scope() as s: ...
    """
    s = session()
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()
