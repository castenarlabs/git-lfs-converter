import auth_prep as auth
from os import chdir, error, popen, getcwd


# Change back to python directory
cur_dir = getcwd()


def chdir_to_pyrepo():
    try:
        chdir(cur_dir)
        # print(getcwd())
    except error() as e:
        print("\u274c Error: Unable to get current directory ", e)


def chdir_to_main_repo():
    try:
        # Change to repo directory
        chdir(auth.repo_path)
    except error() as e:
        print("\u274c Error: Unable to change directory to repo directory ", e)


def install_lfs():
    try:
        chdir_to_main_repo()
        # print('\n', os.getcwd())
        print("\n######## Initializing GIT LFS Install ##########")
        print(popen('git lfs install').read())
        print("\n######## Listing GIT LFS Configs ##########\n")
        print(popen('git lfs env | awk FNR!=4').read()) # This line excludes LFS Endpoint row as it contains the App Password which is appended to the URL
        chdir_to_pyrepo()
        # print('\n', getcwd())
    except error() as e:
        print("\u274c Error: ", e)
