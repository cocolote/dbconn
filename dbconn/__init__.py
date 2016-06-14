# -*- coding: utf-8 -*-

import sys
import urllib
import yaml

import sqlalchemy as sa
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


__author__ = 'Ezequiel Lopez'
__email__ = 'skiel.j.lopez@gmail.com'
__version__ = '0.0.1'


class DBconn():
    '''
    Class to handle the connections and session with the DB

    how to use it: instantiate the DBconn class with two parameters
        1) path to the db_conf.yml file
        2) code_status, for example, DEV to connect to the DEV DB.

    From the class you can get the Base class already associated to
    the engine, a session and a session_scope to use on a with statement
    '''
    # TODO: add logging to the library
    # TODO: seems like there might be a class here even though it might make
    # more sense to just have methods that get called from the dbconn module
    # directly.

    def __init__(self, db_conf, dbconf_path=''):
        '''
        :param db_conf: path to YAML DB config file
        :param dbconf_path: path to YAML DB config file
        '''
        # TODO: figure out params ... these both seem to be for the same
        # purpose but one of them does nothing.
        self.db_conf = db_conf.upper()
        self.engine = sa.create_engine(self.get_connection_string())

    def get_connection_string(self):

        with open('dbconf.yml') as f:
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
                server=conf[self.db_conf]['SERVER'],
                port=conf[self.db_conf]['PORT'],
                db=conf[self.db_conf]['DBNAME'],
                uid=conf[self.db_conf]['USERNAME'],
                pwd=conf[self.db_conf]['PASSWORD'],
                tds_v=conf[self.db_conf]['TDS_VERSION']
            ))
        else:
            # TODO: check this .. this does not look right for Windows
            # what happens if the user has Mac?
            return 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus((
                'DRIVER=FreeTDS;'
                'SERVER={server};'
                'PORT={port};'
                'DATABASE={db};'
                'UID={uid};'
                'PWD={pwd};'
            ).format(
                server=conf[self.db_conf]['SERVER'],
                port=conf[self.db_conf]['PORT'],
                db=conf[self.db_conf]['DBNAME'],
                uid=conf[self.db_conf]['USERNAME'],
                pwd=conf[self.db_conf]['PASSWORD'],
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
