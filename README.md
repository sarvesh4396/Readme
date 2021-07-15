# Readme

Only CLI Package you need to your all Readme.

![PyPI version](https://img.shields.io/pypi/v/Readme?color=orange&logo=pypi&logoColor=orange&style=flat-square)
![Language](https://img.shields.io/badge/python-3.7%2B-blue?logo=python&style=flat-square)
[![GitHub issues](https://img.shields.io/github/issues/sarvesh4396/Readme)](https://github.com/sarvesh4396/Readme/issues)
[![GitHub forks](https://img.shields.io/github/forks/sarvesh4396/Readme)](https://github.com/sarvesh4396/Readme/network)
[![GitHub stars](https://img.shields.io/github/stars/sarvesh4396/Readme)](https://github.com/sarvesh4396/Readme/stargazers)
[![GitHub license](https://img.shields.io/github/license/sarvesh4396/Readme)](https://github.com/sarvesh4396/Readme/blob/main/LICENSE)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/sarvesh4396/Readme/main?label=updated)
![Pull Requests](https://img.shields.io/badge/PRs-welcome-organge.svg?logo=git&logoColor=organge&style=flat-square)

## What it Does

> It creates a repository named `Readme` in your local storage with all readme of your github account.

## Requirements

- Github Account
- Github Access Token

## Installation

Readme requires [python3.7+](https://www.python.org/downloads/) to run.

### Windows

```sh
pip install readme
or
pip install --upgrade readme
```

### Linux

```sh
pip3 install readme
or 
pip3 install --upgrade readme
```

## CLI Usage

```sh
usage: Readme [-h] -u U --secret SECRET [--forked] [-p P]

Only CLI Package you need to your all Readme.

optional arguments:
  -h, --help       show this help message and exit
  -u U             Github username.
  --secret SECRET  Github secret.
  --forked         Includes forked repositories.
  -p P             Set Path to store Readme files.
```

## Example

```sh

readme -u sarvesh4396 --secret ************

```
