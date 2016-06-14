=====
Usage
=====

To use SQL Connection Wrapper in a project::

    import dbconn

    conn = dbconn.DBConn('dev')
    Base = conn.Base()

    # build your models using the declarative base from dbconn:
    class MyModel(Base):
        __tablename__ = 'MyModel'
        __table_args__ = {'autoload': True}

    # use the connection to get a session:
    session = conn.get_session()
    # ... do session queries here ...
    session.query(...).all()
    # and don't forget to close the session!
    session.close()

    # use the built in transaction scope:
    with conn.transaction_scope() as session:
        # make queries here...
        result = session.query(...).first()
        # session commit or rollback taken care of for you depending on errors

You will need to create a dbconf YAML file using the specs::

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

