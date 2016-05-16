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
###Requirements
- Python 3.4
- pyodbc 3.0.10
- PyYAML 3.11
- SQLAlchemy 1.0.12

###Installation
- Clone the repo.
- In the dbconn execute this command:
```
$ python setup.py sdist
```
This will create a distribution file that you can use to install the module
into the your application's virtual enviroment

- To install the module run this code with your virtual environment activated:
```
$ pip install path/to/clone/repo/dbconn/dist/dbcon/dbconn-0.0.1.tar.gz
```
- After the installations is completed, run this command to see if the module
  was installed in your virtual env.
```
$ pip freeze
dbconn==0.0.1
```
---

###Configuration
Add a __dbconf.yaml__ like this to your project:

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
