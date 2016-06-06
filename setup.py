from setuptools import setup, find_packages
from subprocess import call
from setuptools.command.install import install
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg
from dbconn.__init__ import APP_NAME, APP_VERSION

class bdist_egg(_bdist_egg):
    def run(self):
        call(['pip install -r requirements.txt --no-clean'], shell=True)
        _bdist_egg.run(self)

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description='Connection to the ATG DB with sqlalchemy',
    author='Ezequiel Lopez',
    author_email='elopez@atg.travel',
    license='PSF',
    packages=find_packages(),

    install_requires=[
        'setuptools',
        'pyodbc>=3.0.10',
        'python-env>=1.0.0',
        'PyYAML>=3.11',
        'SQLAlchemy>=1.0.12',
    ],

    cmdclass={ 'bdist_egg': bdist_egg },
  )
