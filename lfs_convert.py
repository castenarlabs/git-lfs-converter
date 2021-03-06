import git
import repo_clone_push
import auth_prep as auth
#import status_branch_check as status_check
import lfs_setup as lfs_setup
import os
import sys
import decouple
from decouple import Csv


def pattern_handler():
    pattern = decouple.config('patterns')

    # Convert String to List and append "*." to each item in the list
    x = pattern.split(",")
    pat_list = []

    for p in x:
        p = ("*." + p)
        #    print(type(p))
        pat_list.append(p)

    global pattern_str
    pattern_str = ",".join(pat_list)
    # print(pattern_str)


# pattern_handler()
# lfs_migrate = "git lfs migrate import --include='" + pattern_str + "' --everything"
# print(lfs_migrate)

def run_lfs_convert():
    # Pattern from .env file (pattern_handler func)
    pattern_handler()
    lfs_migrate = "git lfs migrate import --include='" + pattern_str + "' --everything"
    # bfg_command = "java -jar bfg.jar --convert-to-git-lfs '*.{" + pattern + "}' --no-blob-protection --private '" + auth.repo_path + "'"
    aggressive_gc = "git reflog expire --expire=now --all && git gc --prune=now --aggressive"
    # push_all = "git push --force --all && git lfs push origin --all"

    # Use BFG to convert files to LFS
    print("\n###################################################")
    print("###  Converting to LFS with Git LFS Migrate Tool  ###")
    print("#####################################################")
    print("\n")
    print("Patterns / Files to convert : ", pattern_str)
    # Change to repo directory
    os.chdir(auth.repo_path)
    print(lfs_migrate)
    print(os.system(lfs_migrate))
    print("\n")

    # Run Aggressive GC
    print("################################")
    print("###  RUNNING AGGRESSIVE GC  ###")
    print("################################")
    print("\n")
    print(aggressive_gc)
    print(os.system(aggressive_gc))
    print("\n")

    # Force Push Repository and LFS files
    print("############################################")
    print("###  Force Push Repository & LFS Objects ###")
    print("############################################")
    print("\n")
    repo_clone_push.lfs_force_push()

    # Change back to lfs converter repo
    lfs_setup.chdir_to_pyrepo()
