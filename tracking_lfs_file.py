import git
import pygit2
from repo_clone_push import repo_path
import os
import logging
import sys
import git_lfs
import subprocess

# Change back to python directory
# #################### Create Dummy Binary file
# dd if=/dev/zero of=ostechnix.txt bs=5 count=1
cur_dir = os.getcwd()


def chdir_to_pyrepo():
    os.chdir(cur_dir)
    print(os.getcwd())


def tracking_lfs():
    try:
        repo = git.Repo(repo_path)
        # print(repo.git.status(), "\n\n")
        print("Check / Lists all of LFS Configurations Exists in config files: ")
        lfs_config_check = os.system('git config --list |grep lfs')
        print(lfs_config_check, "\n\n")

        # Change to repo directory
        os.chdir(repo_path)
        # print(os.getcwd())
    
        # Track LFS files based on Pattern
        patterns = []
        data_valid = False

        while data_valid == False:
            try:
                i = int(input("How many patterns do you want to enter: "))
                data_valid = True
            except ValueError as Val_Error:
                print("Error: Please enter INTEGER Only ")

        x = int(0)
        while x < i:
            new_pattern = input("State a pattern for a file you want to track: ")
            patterns.append(new_pattern)
            x += 1
    
        print("\n")
        pat_len = len(patterns)
        i = 0
    
        while i < pat_len:
            # print(patterns[i])
            track = os.system("git lfs track '*." + patterns[i] + "'")
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
    
    
    
# print("ConfigReader: \n")

# config_reader.items_all('<section>')
# print(type(config_reader.items_all('filter "lfs"')))
# print(config_reader.items_all('filter "lfs"'), "\n")

# print(repo.git.status())


# print(repo.config_reader(config_level="user"))
# logging.basicConfig(level=logging.DEBUG)

# print(os.system("pwd"))
# stage = r.index.add([".gitattributes"])
# committing = r.index.commit("Tracking LFS files via '.gitattributes' file ")
# print(stage, "\n")
# print("The latest commit hash is :", committing)

# repo = git.Repo(repo_path)
# print(repo.git.status())


# print(os.system("pwd"))
# stage = repo.git.add([".gitattributes"])
# committing = repo.git.commit(m='Tracking LFS files via .gitattributes file')
# print(stage, "\n")
# print("The latest commit hash is :", committing)
