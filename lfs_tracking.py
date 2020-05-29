import git
from repo_clone import repo_path
import os
import logging
import sys

repo = git.Repo.init(repo_path)
config_reader = repo.config_reader()

# Verify Git Author for Commit
print("The Configured GitAuthor is: ", config_reader.get_value("user", "name"))
print("The configured Git Email is: ", config_reader.get_value("user", "email"), "\n")

print(repo_path, "\n\n")

print("###### CURRENT STATUS ######")
print(repo.git.status())
print("############################\n\n")

# Check Current branch. Enter "<branch_name>" to create new branch. ('<flag>', "<branch_name>")
branch_chk = repo.git.branch()
print("###### LIST OF BRANCH ######")
print(branch_chk)
print("############################\n\n")
# print(type(branch_chk))

switch_branch = input("Do you want to switch branches (Yes or No): ").lower()
#switch_branch = "no"

if switch_branch == 'yes':
    branch_name = input("Which branch listed above that you would like to checkout: ").lower()
    checkout = repo.git.checkout(branch_name)
    branch = repo.git.branch()
    x = branch.splitlines()
    # print(type(x))
    #print(x, "##########\n\n")

    for string in x:
        if string[0] == '*':
            # print("######## PRINT BRANCH currently checked out#########")
            print("The branch which you will be working on is: ", string[2:])
else:
    branch = repo.git.branch()
    x = branch.splitlines()

    for string in x:
        if string[0] == '*':
            # print("######## ELSE #########")
            print("The branch which you will be working on is: ", string[2:])





#print(checkout)


# print(os.system("pwd"))
# lfs_config_check = os.system("git config --list |grep lfs")
# print(lfs_config_check, "\n")

# os.chdir(repo_path)
# print(os.system("pwd"))

# track_lfs = os.system("git lfs track 'png'")
# print(track_lfs, "\n")
# print(os.system("cat .gitattributes"), "\n")


#print("ConfigReader: \n")

# config_reader.items_all('<section>')
#print(type(config_reader.items_all('filter "lfs"')))
#print(config_reader.items_all('filter "lfs"'), "\n")

#print(repo.git.status())


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
