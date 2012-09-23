#!/usr/bin/env python
import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'pydi'
]

requires = []

setup(
    name='pydi',
    version='0.2.1',
    description='Little Dependency Injection Container',
    long_description=open('README.md').read(),
    author='Adam Venturella',
    author_email='aventurella@gmail.com',
    url='http://github.com/aventurella/pydi',
    license=open('LICENSE').read(),
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    package_dir={'pydi': 'pydi'},
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
    ),

)

del os.environ['PYTHONDONTWRITEBYTECODE']
