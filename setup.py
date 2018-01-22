#!/usr/bin/env python

from pydgutils_bootstrap import use_pydgutils
use_pydgutils()

import os
import os.path
import sys
import shutil
import logging
import fnmatch
import pydgutils
import pydgutils.version
from setuptools import setup, find_packages

package_name = "docker-maintain"

our_packages, source_dir = pydgutils.process_packages()
our_requires = pydgutils.process_requirements()

long_description = (
    open("README.rst", "r").read()
    + "\n" +
    open("CHANGES.rst", "r").read()
)

setup(
    name=package_name,
    version='0.1.0',
    author="Hong-She Liang",
    author_email="starofrainnight@gmail.com",
    url="https://github.com/starofrainnight/%s" % package_name,
    description="",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=our_requires,
    package_dir={"": source_dir},
    packages=our_packages,
    entry_points={
        'console_scripts': [
            'docker-maintain = docker_maintain.__main__:main'
        ]
    },
    # If we don"t set the zip_safe to False, pip can"t find us.
    zip_safe=False,
)
