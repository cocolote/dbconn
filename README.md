#MS SQL DB connection class SQLAlchemy
---
Easy to use class to connect your application in python with a Microsoft SQL
Database using SQLAlchemy.

The class is ready to handle the connection from a Windows computer or a Linux
machine. It detects your system automatically.

Once instantiated, the object has two helful methods
1. Base: it returns a Base object generated with your configuration of the DB,
   ready to use in your models

2. get_session: it returns a session object ready to execute queries within
   your DB.

Also the module has a second class __CtrlSession__ that can be use in a
__with__ clause to execute queries that depending on the response from the
server it will commit it, rollback or close the session.

Exampl:
```
with CtrlSession() as session:
    result = session.query(MyModel).all()
```
---

### Quick Start

Install via pip:

    $ pip install dbconn

---

###Configuration
Add a __dbconf.yml__ like this to your project:

```
DEV:
  SERVER: <server name>
  DBNAME: <database name>
  PORT: <database port>
  TDS_VERSION: <tds version for your server>
  USERNAME: <username>
  PASSWORD: <password>

PROD:
  SERVER: <server name>
  DBNAME: <database name>
  PORT: <database port>
  TDS_VERSION: <tds version for your server>
  USERNAME: <username>
  PASSWORD: <password>
```
The configuration file will be read from the root directory of you app.

Instantiate a DBconn object with the DB that you want to use. In the example
I'm using the DEV DB configuration.
```
conn = DBconn('dev')
```
Then with this object you can request a Base object to use in your models
```
Base = conn.Base()
```

You can override the location of the dbconf file:
```
conn = DBconn('prod', '/path/to/conf/file.yml')
Base = conn.Base()
```

