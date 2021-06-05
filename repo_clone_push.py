# This file is to define functions to clone a repository and to clone a bare repository inclusive of pushes

import git
import decouple
from decouple import Csv
import os
import auth_prep as auth
from os import path, error, system
import shutil


push_all = "git push --force && git lfs push origin --all"


class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print('Cloning Progress ===== (op_code= %s, cur_count = %s, max_count= %s, message= %s)' % (op_code, cur_count, max_count, message))


def clone(is_bare):
    try:
        if not is_bare:
            print("\nCloning Non-Mirror Repository")
            (git.Repo.clone_from(auth.full_repo_url, auth.repo_path, mirror=False))
            print("\n\u2714 Repository Cloned Successfully")
            print("\n")
        else:
            print("\n\u2714 Cloning Mirror Repository")
            git.Repo.clone_from(auth.full_repo_url, auth.repo_path, mirror=True, progress=Progress())
            print("\n\u2714 Mirror Repository Cloned Successfully")
    except git.exc.GitError as GitError:
        print("\n\u274c ERROR: \n", GitError)
        exit(1)


def backup_path_construct():
    try:
        global backup_path
        if auth.repo_path[-1] == '/':
            backup_path = auth.repo_path[:-1] + "_backup"
        else:
            backup_path = auth.repo_path + "_backup"
    except error as Error:
        print("\n\u274c Error:\n Couldn't construct repository backup path :( \n", Error)


def backup_repo():
    try:
        shutil.copytree(auth.repo_path, backup_path)
        print("\u2714 Backup Made Successfully At:'", backup_path, "'")
    except error as Error:
        print("\n\u274c Error:\n Couldn't make repository backup :( \n", Error)


def clone_dir_rm():
    try:
        print('Checking if Clone Directory already exists or not. If yes, remove existing directory')
        if str(path.exists(auth.repo_path)) == 'True':
            shutil.rmtree(auth.repo_path)
            print("\u2714 Removing Existing Directory")
        else:
            print("\u2714 No Existing Dir Matching : ", auth.repo_path, "\nChecking if Backup Directory exists. If yes, remove existing directory")

        if str(path.exists(backup_path)) == 'True':
            shutil.rmtree(backup_path)
            print("\u2714 Removing Existing Backup Directory")
        else:
            print("\u2714 No Existing Backup Dir Matching : ", backup_path, "\nProceeding with Mirror Repository Clone")

    except OSError as error:
        print(error)
        exit(1)


def push():
    try:
        repo = git.Repo(auth.repo_path)
        g = git.cmd.Git(auth.repo_path)
        print(repo.git.push('origin', "-vv", verbose=True))
    except git.exc.GitError as GitError:
        print("\u274c Error: \n", GitError)


def lfs_force_push():
    try:
        # print(push_all)
        print("Script is PAUSED. Pending user inspection and input.\nNow You can access the bare repository to check the LFS files count using 'git lfs ls-files -a'."
              "\nType 'yes' to continue force push to original repo (Anything else will exit the program:")
        inp = input()
        if inp == 'yes':
            print("Proceeding with Force Push : \n")
            print(system(push_all))
        else:
            print("Exiting the program. You will need to manually perform the force push using 'git push --force' from the same directory the repository was cloned")
            exit(1)
    except git.exc.GitError as GitError:
        print("\u274c Error: \n", GitError)
        exit(1)
