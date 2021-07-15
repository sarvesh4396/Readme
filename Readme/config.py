from pathlib import Path

# Variables
README = "Readme"
HOMEDIR = str(Path.home())
REPO_STRING = "- [{}]({}) {}\n"  # Format-type -> Reponame,Repourl,Description
REPOCARD_URL = "[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username={}&repo={})]({})\n\n"  # Format-type -> Username, Reponame, REPO_URL

# Package Requirements
INSTALL_REQUIRES = ["PyGithub", "tqdm"]

# Package meta-data.
NAME = "Readme"
DESCRIPTION = "Only CLI Package you need to your all Readme."
AUTHOR = "Sarvesh Kumar Dwivedi"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "0.0.1"