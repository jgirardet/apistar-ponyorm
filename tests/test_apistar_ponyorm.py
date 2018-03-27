# Third Party Libraries
import pytest
from apistar import App, Route, TestClient
from pony.orm import Database, Required, TransactionError

# apistar_ponyorm
from apistar_ponyorm import ponydb_close, ponydb_exception, ponydb_open

"""
ponyorm setup
"""

db = Database()


class A(db.Entity):
    aaa = Required(str)


db.connect(
    provider="sqlite",
    filename=":memory:",
    create_tables=True,
)
""" 
    Apistar Main App
"""


def create() -> dict:
    a = db.A(aaa="some string")
    b = db.A[1]
    return b.to_dict()


route = Route(url="/", method="GET", handler=create)


def test_fail_without_before_handler():
    app = App(routes=[route])
    cli = TestClient(app)
    with pytest.raises(TransactionError) as e:
        cli.get('/')
    assert str(
        e.value) == "db_session is required when working with the database"


app = App(
    routes=[route],
    run_before_handler=[ponydb_open],
    run_after_handler=[ponydb_close],
    run_on_exception=[ponydb_exception],
)

cli = TestClient(app)


def test_success_with_before_and_after():
    r = cli.get('/')
    assert r.json() == {'id': 1, "aaa": "some string"}


def test_exception_close_db():
    r = cli.get('/fzefzefzef/')
    assert r.json() == 'Not found'
