#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = [
    'pydi'
]

requires = []

setup(
    name='pydi',
    version='0.1',
    description='Little Dependency Injection Container',
    long_description=readme,
    author='Adam Venturella',
    author_email='aventurella@gmail.com',
    url='http://github.com/aventurella/pydi',
    license=license,
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
