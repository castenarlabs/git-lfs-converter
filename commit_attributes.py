import git
import pygit2
import repo_clone_push
import auth_prep as auth
import status_branch_check as status_check
import os
import logging
import sys
import subprocess


def commit_attr():
    repo = git.Repo(auth.repo_path)
    # Checking Git Status
    status_check.status_check()

    print("Staging")
    print(repo.git.add('.gitattributes'), "\n")

    print("Committing")
    print(repo.git.commit(message="Adding LFS Tracking via .gitattributes'"), "\n")
    print(repo.git.status())


# commit_attr()
