#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_helpscout

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_helpscout.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-helpscout',
    version=version,
    description="""Help Scout integration for Django""",
    long_description=readme + '\n\n' + history,
    author='Victor Neo',
    author_email='icyisamu@gmail.com',
    url='https://github.com/victorneo/Django-Helpscout',
    packages=[
        'django_helpscout',
    ],
    include_package_data=True,
    install_requires=[
        'django',
        'six',
    ],
    license="Apache License V2",
    zip_safe=False,
    keywords='Django-Helpscout, Django, Help Scout',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
