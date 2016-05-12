from distutils.core import setup
from setuptools import find_packages
from dbconn.__init__ import APP_NAME, APP_VERSION

setup(name=APP_NAME,
      version=APP_VERSION,
      description='Connection to the ATG DB with sqlalchemy',
      author='Ezequiel Lopez',
      author_email='elopez@atg.travel',
      packages=find_packages(),
  )
