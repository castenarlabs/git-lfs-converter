import repo_clone_push  # from file repo_clone_push.py
# from repo_clone import repo_path
import status_branch_check as status_branch  # this is to get branch/status check function for a non bare repository
import tracking_lfs_file as track_lfs
import commit_attributes as committing
import lfs_convert_bfg as lfs_convert
import logging
import auth_prep as auth
import env_file_check as check

#Check to ensure all env are defined
check.env_check()
auth.auth_prep()

bare = input("Do you want to Clone a bare repository (Enter Yes or No): ").lower()

while True:
    if bare == "yes":
        is_bare = True
        repo_clone_push.clone(is_bare)
        lfs_convert.run_bfg_convert()
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
