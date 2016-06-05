import sys
import urllib
import yaml

import pyodbc
import sqlalchemy as sa
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# DECLARATIONS FOR SETUP.PY
APP_NAME = 'dbconn'
__versionnum__ = ('0', '0', '1')
APP_VERSION = '.'.join([i for i in __versionnum__])

# CONNECTION CLASS
class DBconn():

    '''
    Class to handle the connections and session with the DB

    how to use it: instantiate the DBconn class with two parameters
        1) path to the db_conf.yaml file
        2) code_status, for example, DEV to connect to the DEV DB.

    From the class you can get the Base class already associated to
    the engine, a session and a session_scope to use on a with statement
    '''

    def __init__(self, db_conf, dbconf_path=''):
        self.db_conf = db_conf.upper()
        self.engine  = sa.create_engine(self.get_connection_string())
        self.dbconf_path = dbconf_path

    def get_connection_string(self):

        with open(self.dbconf_path+'dbconf.yaml') as f:
            conf = yaml.safe_load(f)

        if sys.platform == 'linux':
            return 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus((
                       'DRIVER=FreeTDS;'
                       'SERVER={server};'
                       'PORT={port};'
                       'DATABASE={db};'
                       'UID={uid};'
                       'PWD={pwd};'
                       'TDS_Version={tds_v};'
                    ).format(
                        server = conf[self.db_conf]['SERVER'],
                        port   = conf[self.db_conf]['PORT'],
                        db     = conf[self.db_conf]['DBNAME'],
                        uid    = conf[self.db_conf]['USERNAME'],
                        pwd    = conf[self.db_conf]['PASSWORD'],
                        tds_v  = conf[self.db_conf]['TDS_VERSION']
                    ))
        else:
            return 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus((
                       'DRIVER=FreeTDS;'
                       'SERVER={server};'
                       'PORT={port};'
                       'DATABASE={db};'
                       'UID={uid};'
                       'PWD={pwd};'
                    ).format(
                        server = conf[self.db_conf]['SERVER'],
                        port   = conf[self.db_conf]['PORT'],
                        db     = conf[self.db_conf]['DBNAME'],
                        uid    = conf[self.db_conf]['USERNAME'],
                        pwd    = conf[self.db_conf]['PASSWORD'],
                    ))

    def Base(self):
        return declarative_base(self.engine)

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    @contextmanager
    def session_scope(self):
        session = self.get_session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
