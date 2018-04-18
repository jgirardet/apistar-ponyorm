# Third Party Libraries
import pony
import pytest
from apistar import App, Route, TestClient
from pony.orm import Database, Required, TransactionError, db_session

# apistar_ponyorm
from apistar_ponyorm import PonyDBSession

"""
ponyorm setup
"""

db = Database()


class A(db.Entity):
    aaa = Required(str)


db.connect(provider="sqlite", filename=":memory:", create_tables=True)
""" 
    Apistar Main App
"""


def create() -> dict:
    a = db.A(aaa="some string")
    b = db.A[1]
    return b.to_dict()


def server_error():
    a = 1 / 0


def server_error_db_session_already_closed():
    db_session.__exit__()
    a = 1 / 0


route = [
    Route(url="/", method="GET", handler=create),
    Route(url="/zerodiv/", method="GET", handler=server_error),
    Route(
        url="/zerodiv_closed/",
        method="GET",
        handler=server_error_db_session_already_closed,
    ),
]


def test_fail_without_on_request():
    app = App(routes=route)
    cli = TestClient(app)
    with pytest.raises(TransactionError) as e:
        r = cli.get("/")
        print(r.json())
    assert str(e.value) == "db_session is required when working with the database"


app = App(routes=route, event_hooks=[PonyDBSession()])

cli = TestClient(app)


def test_success_with_on_and_after():
    r = cli.get("/")
    assert r.json() == {"id": 1, "aaa": "some string"}


def test_error_close_db():
    r = cli.get("/fzefzefzef/")

    assert r.json() == "Not found"


def test_fail_if_not_found():
    if pony.orm.core.local.db_session is not None:
        db.__exit__()
        r = cli.get("/")
    r = cli.get("/")
    r = cli.get("/fzefze/")
    r = cli.get("/")
    assert r.status_code == 200


def test_server_error():
    try:
        r = cli.get("/zerodiv/")
    except ZeroDivisionError:
        pass
    assert pony.orm.core.local.db_session is None


def test_server_error_bd_already_closed():
    try:
        r = cli.get("/zerodiv_closed/")
    except ZeroDivisionError:
        pass
    assert pony.orm.core.local.db_session is None
