import git
from repo_clone_push import repo_path
import status_branch_check as status_check
import tracking_lfs_file as tracking_lfs
import os
import sys


def run_bfg_convert():
    bfg_command = "java -jar bfg.jar --convert-to-git-lfs '*.jpg' --no-blob-protection --private '" + repo_path + "'"
    aggressive_gc = "git reflog expire --expire=now --all && git gc --prune=now --aggressive"
    push_all = "git push --force --all && git lfs push origin --all"

    # Use BFG to convert files to LFS
    print("#########################################")
    print("###  Converting to LFS with BFG Tool  ###")
    print("#########################################")
    print("\n")
    print(bfg_command)
    print(os.system(bfg_command))
    print("\n")
    # Change to repo directory
    os.chdir(repo_path)
    #print(os.getcwd())

    # Run Aggressive GC
    print("################################")
    print("###  RUNNING AGGRESSIVE GC  ###")
    print("################################")
    print("\n")
    print(aggressive_gc)
    print(os.system(aggressive_gc))
    print("\n")
    # Force Push Repository and LFS files
    # git push --force --all && git lfs push origin --all
    print("############################################")
    print("###  Force Push Repository & LFS Objects ###")
    print("############################################")
    print("\n")
    print(push_all)
    print(os.system(push_all))

    # Change back to lfs converter repo
    tracking_lfs.chdir_to_pyrepo()


run_bfg_convert()
