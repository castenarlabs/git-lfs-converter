import repo_clone_push  # from file repo_clone_push.py
import lfs_setup as lfs_setup
import lfs_convert as lfs_convert
import auth_prep as auth
from repo_clone_push import clone_dir_rm
from datetime import datetime
from summary import script_summary


# Time Function
def get_time_utc():
    global time
    time = (datetime.utcnow())


get_time_utc()
start_time = time
print("\nStart Time", start_time, "\n")

is_bare = True  # Clone Bare Repo
repo_clone_push.backup_path_construct()  # Constructing Repository Backup Path
clone_dir_rm()  # Remove Existing Clone Dir before fresh clone
repo_clone_push.clone(is_bare)  # Cloning the bare repo)
repo_clone_push.backup_repo()  # Backing Up the Repo
lfs_setup.install_lfs()  # Initializing LFS in the repo
lfs_convert.run_lfs_convert()  # Converting to LFS using "GIT LFS MIGRATE" including a FORCE PUSH option
script_summary()

get_time_utc()
end_time = time
print("\nEnd Time", end_time)
duration = str(end_time - start_time).split(".")[0]
print("Total Script Time :", duration)
