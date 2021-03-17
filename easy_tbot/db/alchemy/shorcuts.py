from ..loader import Backend
from sqlalchemy.orm import Session as SQlAlchemySession
from contextlib import contextmanager

__backend = Backend()


Model = __backend.model
Session = __backend.session

@contextmanager
def session_scope() -> SQlAlchemySession:
    """
    A context for sections, for properly management of our section.
    Example: with session_scope() as s: ...
    """
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
