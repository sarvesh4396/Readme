#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os import makedirs
from os.path import join
from genericpath import exists
from github import Github
from tqdm import trange
from Readme.config import DESCRIPTION, HOMEDIR, README, REPO_STRING, REPOCARD_URL


class Repo:
    def __init__(self, username, secret):
        self.username = username
        self.secret = secret
        self.g = Github(username, secret)

    def repositories(self):
        return list(self.g.get_user().get_repos())

    def readme(self, repo_name):
        repo = self.g.get_user().get_repo(repo_name)
        file = repo.get_contents("README.md")
        return file.decoded_content.decode("utf-8")


class Readme:
    def __init__(self, username, secret, base_path, fork):
        self.fork = fork
        self.username = username
        self.secret = secret
        self.base_path = base_path
        self.git = Repo(username, secret)

    def process_readme_metadata(self):
        repo_url = self.repo.html_url
        reponame = self.repo.name

        repo_card = REPOCARD_URL.format(self.username, reponame, repo_url)

        # Storing Path
        self.path = join(self.base_path, reponame + ".md")

        self.writing_data = repo_card + self.writing_data

    def get_readme(self):
        repo_name = self.repo.name
        self.writing_data = self.git.readme(repo_name)

    def write_readme(self):
        with open(self.path, "w", encoding="utf-8", errors="ignore") as readme:
            readme.write(self.writing_data)

    def filter_repository(self):
        if not self.fork:
            print("Filtering repositories on the basis of fork property...")
            filtered_repos = []
            for repo in self.all_repo:
                if not repo.fork:
                    filtered_repos.append(repo)

            print(f"Found {len(filtered_repos)} repositories after filtering.")
            self.all_repo = filtered_repos

    def main_readme(self):
        print("Generating README.md of Readme repository.")

        self.writing_data = "# Repositories\n"

        for i in trange(len(self.all_repo)):
            repo = self.all_repo[i]
            description = repo.description or " "
            self.writing_data += REPO_STRING.format(
                repo.name, repo.html_url, description
            )
        self.path = join(self.base_path, "README.md")
        self.write_readme()

    def run(self):
        self.all_repo = self.git.repositories()
        print(f"Found {len(self.all_repo)} repositories.")

        self.filter_repository()

        print("Generating Repositories Readme.")

        for i in trange(len(self.all_repo)):
            self.repo = self.all_repo[i]
            self.get_readme()
            self.process_readme_metadata()
            self.write_readme()
        self.main_readme()


def get_args():
    parser = ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-u",
        help="Github username.",
        required=True,
    )
    parser.add_argument(
        "--secret",
        help="Github secret.",
        required=True,
    )
    parser.add_argument(
        "--forked",
        help="Includes forked repositories.",
        action="store_true",
    )
    parser.add_argument(
        "-p",
        help="Set Path to store Readme files.",
    )

    args = parser.parse_args()

    if not any(vars(args).values()):
        print("\n" + parser.format_help())
        exit(0)

    return args


def main():
    args = get_args()

    if args.p:
        args.p = join(args.p, README)
    else:
        args.p = join(HOMEDIR, README, README)

    if not exists(args.p):
        makedirs(args.p)

    Readme(
        username=args.u,
        secret=args.secret,
        base_path=args.p,
        fork=args.forked,
    ).run()
    print(f"Your new repository is stored at {args.p}")
