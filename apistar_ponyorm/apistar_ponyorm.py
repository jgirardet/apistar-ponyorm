import contextlib
import typing

from pony.orm import db_session, Database

from apistar import Command, Component
from config import settings

# db = Database()
# db.bind(**database_config)
# db.generate_mapping(create_tables=True)

from importlib import import_module

db = Database()

for app in settings.INSTALLED_APPS:
    import_module('mapistar.patients.models')

db.bind(**settings.DATABASE)
db.generate_mapping(create_tables=True)

# class PonyBackend(object):
#     pass


@contextlib.contextmanager
def get_session() -> typing.Generator[Database, None, None]:
    """
    Create a new context-managed database session, which automatically
    handles rollback or commit behavior.
    Args:
      backend: The configured database backend.
    """

    with db_session:
        yield db


# def create_tables(backend: SQLAlchemyBackend):
#     """
#     Create all database tables.
#     Args:
#       backend: The configured database backend.
#     """
#     backend.metadata.create_all(backend.engine)

# def drop_tables(backend: SQLAlchemyBackend):
#     """
#     Drop all database tables.
#     Args:
#       backend: The configured database backend.
#     """
#     backend.metadata.drop_all(backend.engine)

components = [
    # Component(PonyBackend),
    Component(Database, init=get_session, preload=False)
]

# commands = [
#     Command('create_tables', create_tables),
#     Command('drop_tables', drop_tables)
# ]