#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

# Variables
README = "Readme"
HOMEDIR = str(Path.home())
REPO_STRING = "- [{}]({}) {}\n"  # Format-type -> Reponame,Repourl,Description
REPOCARD_URL = "[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username={}&repo={})]({})\n\n"  # Format-type -> Username, Reponame, REPO_URL

# Package Requirements
INSTALL_REQUIRES = ["PyGithub", "tqdm"]

# Package meta-data.
NAME = "one_readme"
AUTHOR = "Sarvesh Kumar Dwivedi"
DESCRIPTION = "Only CLI Package you need to manage all your Readme."
GIT_URL = "https://github.com/sarvesh4396/Readme"
KEYWORDS = [NAME, NAME.lower(), "Github"]
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "0.2"
# TODO: CHANGE
DOWNLOAD_URL = (
    f"https://github.com/sarvesh4396/Readme/archive/refs/tags/v{VERSION}.tar.gz"
)
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Topic :: Internet",
    "Topic :: Utilities",
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Version Control :: Git",
    "Environment :: Console",
    "Topic :: Communications :: File Sharing",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: PyPy",
]


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()
    return long_description
