#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'sqlalchemy>=1.0.12',
    'pyodbc>=3.0.10',
    'pyyaml>=3.11',
    'python-env>=1.0.0',
    # TODO: put package requirements here
]

test_requirements = [
    'pytest>=2.9.2',
    # TODO: put package test requirements here
]

setup(
    name='dbconn',
    version='0.0.1',
    description="Easy to use connection library for SQL databases.",
    long_description=readme + '\n\n' + history,
    author="Ezequiel Lopez, Chris Coe",
    author_email='skiel.j.lopez@gmail.com, chrcoe01@gmail.com',
    url='https://github.com/cocolote/dbconn',
    packages=[
        'dbconn',
    ],
    package_dir={'dbconn':
                 'dbconn'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='dbconn',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
