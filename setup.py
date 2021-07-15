#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from Readme.config import (AUTHOR, DESCRIPTION, INSTALL_REQUIRES, NAME,
                                 REQUIRES_PYTHON, VERSION)

setup(
    name=NAME,
    packages=[NAME],
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    install_requires=INSTALL_REQUIRES,
    entry_points={"console_scripts": [f"{NAME} = {NAME}.{NAME.lower()}:main"]},
)
