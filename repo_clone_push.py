# This file is to define functions to clone a repository and to clone a bare repository inclusive of pushes

import git
import decouple
from decouple import Csv
import os
import auth_prep as auth
from os import path
import shutil

# https_repo_url = decouple.config('https_repo_url')
# repo_path = decouple.config('repo_path')
# https_repo_url = "https://castenar@bitbucket.org/castenar/jenkins-test.git"
# repo_path = "/Users/pravin/Documents/Python/TESTCLONE/"
push_all = "git push --force --all && git lfs push origin --all"


# https_repo_url = input("Enter Repo URL from which you want to clone: ")
# repo_path = input("Enter Path to Clone Repository: ")


def clone(is_bare):
    try:
        # https_repo_url = input("Enter Repo URL from which you want to clone: ")
        # auth.repo_path = input("Enter Path to Clone Repository: ")
        if not is_bare:
            print("Cloning Non-Mirror Repository")
            (git.Repo.clone_from(auth.full_repo_url, auth.repo_path, mirror=False))
            print("Repository Cloned Successfully")
            print("\n")
        else:
            print("Cloning Mirror Repository")
            git.Repo.clone_from(auth.full_repo_url, auth.repo_path, mirror=True)
            print("Mirror Repository Cloned Successfully")
    except git.exc.GitError as GitError:
        print("\n ERROR: \n", GitError)
        exit(1)


def backup_path_construct():
    try:
        global backup_path
        if auth.repo_path[-1] == '/':
            backup_path = auth.repo_path[:-1] + "_backup"
        else:
            backup_path = auth.repo_path + "_backup"
    except os.error as Error:
        print("\nError:\n Couldn't construct repository backup path :( \n", Error)


def backup_repo():
    try:
        shutil.copytree(auth.repo_path, backup_path)
        print("Backup Made Successfully At:", backup_path)
    except os.error as Error:
        print("\nError:\n Couldn't make repository backup :( \n", Error)


def clone_dir_rm():
    try:
        print('Checking if Clone Directory already exists or not. If yes, remove existing directory')
        if str(path.exists(auth.repo_path)) == 'True':
            shutil.rmtree(auth.repo_path)
            print("Removing Existing Directory")
        else:
            print("No Existing Dir Matching : ", auth.repo_path, "\nChecking if Backup Directory exists. If yes, remove existing directory")

        if str(path.exists(backup_path)) == 'True':
            shutil.rmtree(backup_path)
            print("Removing Existing Backup Directory")
        else:
            print("No Existing Backup Dir Matching : ", backup_path, "\nProceeding with Mirror Repository Clone")

    except OSError as error:
        print(error)
        exit(1)


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
        print("Script is PAUSED. Pending user inspection and input.\nNow You can access the bare repository to check the LFS files count using 'git lfs ls-files -a'.")
        inp = input("Type 'yes' to continue force push to original repo (Anything else will exit the program): ")
        if inp == 'yes':
            print(os.system(push_all))
        else:
            print("Exiting the program. You will need to manually perform the force push using 'git push --force' from the same directory the repository was cloned")
            exit(1)
    except git.exc.GitError as GitError:
        print("Error: \n", GitError)
        exit(1)
