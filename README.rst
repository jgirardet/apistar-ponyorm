apistar-ponyorm
###########################

.. image:: https://travis-ci.org/jgirardet/apistar_ponyorm.svg?branch=master
    :target: https://travis-ci.org/jgirardet/apistar_ponyorm
.. image:: https://coveralls.io/repos/github/jgirardet/apistar_ponyorm/badge.svg
   :target: https://coveralls.io/github/jgirardet/apistar_ponyorm
.. image:: https://badge.fury.io/py/apistar_ponyorm.svg
   :target: https://pypi.python.org/pypi/apistar_ponyorm/
   :alt: Pypi package


**Third-party for apistar using pony orm**

* License : GNU General Public License v3 
* Documentation: https://apistar_ponyorm.readthedocs.org/en/latest/
* Source: https://github.com/jgirardet/apistar-ponyorm

Features
**********

- Apistar Hook : PonyDBSession which give auto apply db_session to views.


Usage
********

This should be added in App declaration :

app = App(routes=[route], event_hooks=[PonyDBSession()])

.. code-block:: python
    
    # main app.py file
    from apistar_ponyorm import PonyDBSession
    # ...
    app = App(routes=[route], event_hooks=[PonyDBSession()])


    # myviews.py
    from myproject import db # PonyORM Database Instance

    def myviews():
      retun db.MyEntity.to_dict()

    # No need to add @db_session


Changelog
**********

0.2.0 : 
  - add PonyDBSession