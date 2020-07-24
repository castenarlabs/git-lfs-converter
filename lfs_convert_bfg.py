import git
import repo_clone_push
from repo_clone_push import repo_path
import status_branch_check as status_check
import tracking_lfs_file as tracking_lfs
import os
import sys
import decouple
from decouple import Csv


def run_bfg_convert():
    # Pattern from .env file
    pattern = decouple.config('patterns')

    bfg_command = "java -jar bfg.jar --convert-to-git-lfs '*.{" + pattern + "}' --no-blob-protection --private '" + repo_path + "'"
    aggressive_gc = "git reflog expire --expire=now --all && git gc --prune=now --aggressive"
    # push_all = "git push --force --all && git lfs push origin --all"

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
    #print(push_all)
    #print(os.system(push_all))
    repo_clone_push.lfs_force_push()

    # Change back to lfs converter repo
    tracking_lfs.chdir_to_pyrepo()

