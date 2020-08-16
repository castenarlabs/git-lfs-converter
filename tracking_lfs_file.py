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
    os.chdir(cur_dir)
    #print(os.getcwd())


def chdir_to_main_repo():
    # Change to repo directory
    os.chdir(auth.repo_path)


def tracking_lfs():
    try:
        # repo = git.Repo(auth.repo_path)
        # print(repo.git.status(), "\n\n")
        print("Check GIT LFS configurations: ")
        lfs_config_check = os.system('git lfs env')
        print(lfs_config_check, "\n\n")

        # Change to repo directory
        chdir_to_main_repo()
    
        # Track LFS files based on Pattern
        pattern = decouple.config('patterns', cast=Csv())
        print(pattern)
        print(type(pattern))

        pattern_len = len(pattern)
        i = 0

        while i < pattern_len:
            # print(patterns[i])
            track = os.system("git lfs track '*." + pattern[i] + "'")
            # print("git lfs track '*." + pattern[i] + "'")
            i += 1

        if i == 0:
            print("No Patterns to Track")
            exit()
        else:
            print("\n .gitattributes file added to repository")

    except git.exc.NoSuchPathError as GitError:
        print("GIT Error : No Such Repository :  ", GitError)
    except OSError as os_error:
        print("Error:", os_error)
    except NameError as name_err :
        print("Error :", name_err)


#tracking_lfs()
#chdir_to_pyrepo()
    
def install_lfs():
    chdir_to_main_repo()
    #print('\n', os.getcwd())
    print("\n######## Initializing GIT LFS Install ##########")
    os.system('git lfs install')
    print("\n######## Listing GIT LFS Configs ##########\n")
    os.system('git lfs env')
    chdir_to_pyrepo()
    #print('\n', os.getcwd())
