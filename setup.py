# Copyright (c) 2008-2013 Simplistix Ltd
# See license.txt for license details.

import os, sys
from ConfigParser import RawConfigParser
from setuptools import setup, find_packages

name = 'testfixtures'
base_dir = os.path.dirname(__file__)

# read test requirements from tox.ini
config = RawConfigParser()
config.read(os.path.join(base_dir, 'tox.ini'))
test_requires = []
for item in config.get('testenv', 'deps').split():
    test_requires.append(item)
# Tox doesn't need itself, but we need it for testing.
test_requires.append('tox')
# If we're on Python 2.5, we need to pin some libraries
if sys.version_info[:2] < (2, 6):
    test_requires.append('manuel<1.6')
    test_requires.append('zope.component<4.0.0dev')
    test_requires.append('zope.event<4.0.0dev')
    test_requires.append('zope.interface>=3.6.0,<4.0dev')
else:
    # an optional dependency, but we want it present in the buildout
    test_requires.append('zope.component')

setup(
    name=name,
    version=file(os.path.join(base_dir,name,'version.txt')).read().strip(),
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="A collection of helpers and mock objects for unit tests and doc tests.",
    long_description=open(os.path.join(base_dir,'docs','description.txt')).read(),
    url='http://www.simplistix.co.uk/software/python/testfixtures',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    ],    
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=test_requires,
        )
    )
