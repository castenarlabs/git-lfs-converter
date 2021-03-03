import repo_clone_push  # from file repo_clone_push.py
import status_branch_check as status_branch  # this is to get branch/status check function for a non bare repository
import tracking_lfs_file as track_lfs
import commit_attributes as committing
import lfs_convert_bfg as lfs_convert
import logging
import auth_prep as auth
from repo_clone_push import clone_dir_rm

bare = input("Do you want to Clone a bare repository (Enter Yes or No): ").lower()

while True:
    if bare == "yes":
        is_bare = True  # Clone Bare Repo
        repo_clone_push.backup_path_construct()  # Constructing Repository Backup Path
        clone_dir_rm()  # Remove Existing Clone Dir before fresh clone
        repo_clone_push.clone(is_bare)  # Cloning the bare repo)
        repo_clone_push.backup_repo()  # Backing Up the Repo
        track_lfs.install_lfs()  # Initializing LFS in the repo
        lfs_convert.run_bfg_convert()  # Converting to LFS using "GIT LFS MIGRATE" including a FORCE PUSH option
        break
    elif bare == "no":
        is_bare = False
        repo_clone_push.clone(is_bare)
        status_branch.non_bare_checks()
        track_lfs.tracking_lfs()
        track_lfs.chdir_to_pyrepo()
        committing.commit_attr()
        repo_clone_push.push()
        break
    else:
        print("Please enter 'YES' OR 'NO': ")
        print(bare)
        bare = input("Do you want to Clone a bare repository (Enter Yes or No): ").lower()
