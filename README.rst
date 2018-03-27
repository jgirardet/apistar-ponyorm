===============================
apistar_ponyorm
===============================

.. image:: https://travis-ci.org/jgirardet/apistar_ponyorm.svg?branch=master
    :target: https://travis-ci.org/jgirardet/apistar_ponyorm
.. image:: https://readthedocs.org/projects/apistar_ponyorm/badge/?version=latest
   :target: http://apistar_ponyorm.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/jgirardet/apistar_ponyorm/badge.svg
   :target: https://coveralls.io/github/jgirardet/apistar_ponyorm
.. image:: https://badge.fury.io/py/apistar_ponyorm.svg
   :target: https://pypi.python.org/pypi/apistar_ponyorm/
   :alt: Pypi package


Third-party for apistar using pony orm


* License : GNU General Public License v3 
* Documentation: https://apistar_ponyorm.readthedocs.org/en/latest/
* Source: https://github.com/jgirardet/apistar_ponyorm

Features
--------

Provide Basase functions to auto use @db_session  in  views.

This should be added in App declaration :
app = App(
    routes=[....],
    run_before_handler=[ponydb_open],
    run_after_handler=[ponydb_close],
    run_on_exception=[ponydb_exception],
    )

It's important to add ponydb_exception to ensure that  database transaction
will be closed carrefuly


* TODO

