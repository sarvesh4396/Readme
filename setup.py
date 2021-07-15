#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from one_readme.config import (
    AUTHOR,
    DESCRIPTION,
    GIT_URL,
    INSTALL_REQUIRES,
    KEYWORDS,
    NAME,
    REQUIRES_PYTHON,
    VERSION,
    get_long_description,
    CLASSIFIERS,
    DOWNLOAD_URL,
)


setup(
    name=NAME,
    packages=[NAME],
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url=GIT_URL,
    python_requires=REQUIRES_PYTHON,
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    keywords=KEYWORDS,
    download_url=DOWNLOAD_URL,
    entry_points={"console_scripts": [f"readme = {NAME}.readme:main"]},
    classifiers=CLASSIFIERS,
)
