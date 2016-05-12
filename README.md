#MS SQL DB connection class
---
Class that handel the connection to the Microsoft SQL Database server.
It uses sqlalchemy and pyodbc.

In your project you will need a dbconf.yaml like this:

```
DEV:
  SERVER: <server name>
  DBNAME: <database name>
  PORT: <database port>
  TDS_VERSION: <tds version for your server>
  USERNAME: <username>
  PASSWORD: <password>
```

This will be converted into a dictionary, so you could
have multyple setup for different DBs. In this example
the setup is for a Development DBs.

Then all you have to do, instanciate the DBconn class with
the name of the configuration:

```
conn = DBconn('dev')
```
---

####Installation

- Clone the repository
- Navigate into the directory (by default would be dbconn)
- Execute this command to create a distribution file:
```
$ python setup.py sdist
```
- With this file you can install the module using pip like this:
```
$ pip install ~/path/to/distro-file/dbconn.tar.gz`
```
