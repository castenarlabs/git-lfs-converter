import git
import pygit2
import repo_clone_push
import auth_prep as auth
import os
import logging
import sys
import git_lfs
import subprocess
import decouple
from decouple import Csv


# Change back to python directory
cur_dir = os.getcwd()


def chdir_to_pyrepo():
    try:
        os.chdir(cur_dir)
        # print(os.getcwd())
    except os.error() as e:
        print("\u274c Error: Unable to get current directory ", e)


def chdir_to_main_repo():
    try:
        # Change to repo directory
        os.chdir(auth.repo_path)
    except os.error() as e:
        print("\u274c Error: Unable to change directory to repo directory ", e)


def install_lfs():
    try:
        chdir_to_main_repo()
        # print('\n', os.getcwd())
        print("\n######## Initializing GIT LFS Install ##########")
        print(os.popen('git lfs install').read())
        print("\n######## Listing GIT LFS Configs ##########\n")
        print(os.popen('git lfs env | awk FNR!=4').read()) # This line excludes LFS Endpoint row as it contains the App Password which is appended to the URL
        chdir_to_pyrepo()
        # print('\n', os.getcwd())
    except os.error() as e:
        print("\u274c Error: ", e)
