# Third Party Libraries
import pytest
from apistar import App, Route, TestClient, exceptions
from pony.orm import Database, Required, db_session, TransactionError

# from apistar_ponyorm import pony_db
"""
ponyorm
"""

db = Database()


class A(db.Entity):
    aaa = Required(str)


db.connect(
    provider="sqlite",
    filename="db.sqlite",
    create_tables=True,
    create_db=True,
    allow_auto_upgrade=True,
)
""" 
    Apistar Main App
"""

# def pony_db(route: Route, app: App):
#     # print(app.injector.resolver_cache)
#     route.handler = db_session(route.handler)
#     return route.handler


def ponydb_open(route: Route, app: App):
    # print(app.injector.resolver_cache)
    db_session.__enter__()
    print('open db')


def ponydb_close(response):
    # print(app.injector.resolver_cache)
    db_session.__exit__()
    print('close db : Exc')
    return response


# @db_session
def create() -> dict:
    a = db.A(aaa="some string")
    b = db.A[1]
    raise exceptions.HTTPException('omkkkkkkkkkkkkkkmokmokmokmok')
    return b.to_dict()


route = Route(url="/", method="GET", handler=create)


def test_create_no_pony_db():
    app = App(routes=[route])
    cli = TestClient(app)
    with pytest.raises(TransactionError) as e:
        cli.get('/')
    assert str(
        e.value) == "db_session is required when working with the database"


def test_create_with_pony_db():
    app = App(
        routes=[route],
        run_before_handler=[ponydb_open],
        run_after_handler=[ponydb_close])
    cli = TestClient(app)
    r = cli.get('/')
    assert r.json() == {'id': 1, "aaa": "some string"}


app = App(
    routes=[route],
    # components=[EssaiComp(), BasicAuthenticator()],
    # run_before_handler=[get_per],
    run_before_handler=[ponydb_open],
    run_after_handler=[ponydb_close],
    # run_on_exception=[ponydb_close],
)


def run_wsgi(app: App,
             host: str = '127.0.0.1',
             port: int = 8080,
             debug: bool = True,
             reloader: bool = True) -> None:  # pragma: nocover
    import werkzeug
    """
    Run the development server.
    Args:
      app: The application instance, which should be a WSGI callable.
      host: The host of the server.
      port: The port of the server.
      debug: Turn the debugger [on|off].
      reloader: Turn the reloader [on|off].
    """

    options = {
        'use_debugger': debug,
        'use_reloader': reloader,
        'extra_files': ['app.py']
    }

    werkzeug.run_simple(host, port, app, **options)


if __name__ == '__main__':
    # app.serve('127.0.0.1', 8080)
    run_wsgi(app)
