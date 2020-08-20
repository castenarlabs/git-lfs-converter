# This file is to define functions to clone a repository and to clone a bare repository

import git
import decouple
from decouple import Csv
import os
import auth_prep as auth

#https_repo_url = decouple.config('https_repo_url')
#repo_path = decouple.config('repo_path')
# https_repo_url = "https://castenar@bitbucket.org/castenar/jenkins-test.git"
#repo_path = "/Users/pravin/Documents/Python/TESTCLONE/"
push_all = "git push --force --all && git lfs push origin --all"

# https_repo_url = input("Enter Repo URL from which you want to clone: ")
# repo_path = input("Enter Path to Clone Repository: ")


def clone(is_bare):
    try:
        # https_repo_url = input("Enter Repo URL from which you want to clone: ")
        # auth.repo_path = input("Enter Path to Clone Repository: ")
        if not is_bare:
            (git.Repo.clone_from(auth.full_repo_url, auth.repo_path, mirror=False))
            print("Repository Cloned Successfully")
            print("\n")
        else:
            git.Repo.clone_from(auth.full_repo_url, auth.repo_path, mirror=True)
            print("Bare Repository Cloned Successfully")
    except git.exc.GitError as GitError:
        print("Error: \n", GitError)


def push():
    try:
        repo = git.Repo(auth.repo_path)
        g = git.cmd.Git(auth.repo_path)
        print(repo.git.push('origin', "-vv", verbose=True))
    except git.exc.GitError as GitError:
        print("Error: \n", GitError)


def lfs_force_push():
    try:
        # print(push_all)
        inp = input("Type 'yes' to continue force push to original repo (Anything else will exit the program): ")
        if inp == 'yes':
            print(os.system(push_all))
        else:
            print("Exiting the program. You will either need to manually perform the push or run the script again to go through the whole process once again")
            exit(1)
    except git.exc.GitError as GitError:
        print("Error: \n", GitError)

#clone(is_bare=False)