from distutils.core import setup
from setuptools import find_packages
from dbconn.__init__ import APP_NAME, APP_VERSION

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description='Connection to the ATG DB with sqlalchemy',
    author='Ezequiel Lopez',
    author_email='elopez@atg.travel',
    license='PSF',
    packages=find_packages(),

    install_requires=[
        'pyodbc>=3.0.10',
        'python-env>=1.0.0',
        'PyYAML>=3.11',
        'SQLAlchemy>=1.0.12',
    ],
  )
