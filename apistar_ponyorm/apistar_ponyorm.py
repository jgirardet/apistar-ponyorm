from pony.orm import db_session
from apistar import Route


# def pony_db(route: Route):
#     route.handler = orm.db_session(route.handler)
def pony_db(route: Route):
    route.handler = db_session(route.handler)


# class PonyBackend(object):

#     def __init__(self, settings: Settings, cmd: CommandLineClient):
#         """
#         Get the settings.PONY dict
#         do imports in INSTALLED_APPS with PROJECT_NAME
#         """
#         self.db = db
#         pony_config = settings['PONY']
#         entities_filename = pony_config.get('entities_filename', "models")

#         for app in pony_config['INSTALLED_APPS']:
#             import_module('.'.join((pony_config['PROJECT_NAME'], app, entities_filename)))

#         self.db.connect(**pony_config['DATABASE'], )
#         # self.db.connect(provider='sqlite', filename="../db.local", create_tables=True)

# @contextlib.contextmanager
# def get_session(backend: PonyBackend) -> typing.Generator[Database, None, None]:
#     """
#     Create a new context-managed database session, which automatically
#     handles rollback or commit behavior.
#     Args:
#       backend: The configured database backend.
#     """

#     with db_session:
#         yield backend.db

# def create_tables(backend: PonyBackend):
#     """
#     Create all database tables.
#     Args:
#       backend: The configured database backend.
#     """
#     print("create")
#     backend.db.create_tables()

# def drop_all_tables(backend: PonyBackend):
#     """
#     Drop all database tables.
#     Args:
#       backend: The configured database backend.
#     """
#     print('drop')
#     try:
#         backend.db.drop_all_tables()
#     except TableIsNotEmpty:
#         response = input("Are you sure you really want to delete EVERYTHING ? (yes/NO)")
#         if response == "yes":
#             backend.db.drop_all_tables(with_all_data=True)
#         else:
#             print(
#                 'Ok, nothing was deleted, but be careful when you you use a keyboard, bad things could happen !!!'
#             )

# components = [
#     Component(PonyBackend),
#     # Component(PonyBackend, init=False, preload=True),
#     Component(Database, init=get_session, preload=False)
# ]

# commands = [
#     Command('create_tables', create_tables),
#     Command('drop_all_tables', drop_all_tables)
# ]
