# Third Party Libraries
from apistar import http
from pony.orm import Database, db_session
import pony
"""
Base functions to auto use @db_session  in  views.

This should be added in App declaration :
app = App(
    routes=[....],
    run_before_handler=[ponydb_open],
    run_after_handler=[ponydb_close],
    run_on_exception=[ponydb_exception],
    )

It's important to add ponydb_exception to ensure that  database transaction
will be closed carrefuly
"""


class PonyDBSession:
    def on_request(self):
        db_session.__enter__()

    def on_response(self, response: http.Response):
        db_session.__exit__()
        return response

    def on_error(self, response: http.Response):
        if pony.orm.core.local.db_session is not None:
            db_session.__exit__()
        return response
