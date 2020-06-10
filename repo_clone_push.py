# This file is to define functions to clone a repository and to clone a bare repository

import git
from git import RemoteProgress

https_repo_url = "https://castenar@bitbucket.org/castenar/jenkins-test.git"
repo_path = "/Users/pravin/Documents/Python/TESTCLONE/"


# https_repo_url = input("Enter Repo URL from which you want to clone: ")
# repo_path = input("Enter Path to Clone Repository: ")

def clone(is_bare):
    try:
        # https_repo_url = input("Enter Repo URL from which you want to clone: ")
        # repo_path = input("Enter Path to Clone Repository: ")
        if not is_bare:
            (git.Repo.clone_from(https_repo_url, repo_path, mirror=False))
            print("Repository Cloned Successfully")
        else:
            git.Repo.clone_from(https_repo_url, repo_path, mirror=True)
            print("Repository Cloned Successfully")
    except git.exc.GitError as GitError:
        print("Error: ", GitError)


def push():
    repo = git.Repo(repo_path)
    g = git.cmd.Git(repo_path)
    print(g.remote(verbose=True), "\n")
    print(repo.git.push('origin', "-v"))

