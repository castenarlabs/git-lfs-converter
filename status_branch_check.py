import git
import pygit2
from git import Repo
import repo_clone_push
import auth_prep as auth
import os
import logging
import sys
import decouple
from decouple import Csv

# os.chdir(auth.repo_path)
# current_working_directory = os.getcwd()
# print(current_working_directory)

def status_check():
    try:
        repo=git.Repo(auth.repo_path)
        print("###### CURRENT STATUS ######")
        print(repo.git.status())
        print("############################\n\n")
    except git.exc.GitError as GitError:
        print("Error: ", GitError)
        # exit(1)


def non_bare_checks():
    try:
        # repo = git.Repo.init(auth.repo_path)
        repo = git.Repo(auth.repo_path)
    # current_working_directory = os.getcwd()
    # print("Current WORK DIR : ", current_working_directory)
        config_reader = repo.config_reader()

    # Verify Git Author for Commit
        print("The Configured GitAuthor is: ", config_reader.get_value("user", "name"))
        print("The configured Git Email is: ", config_reader.get_value("user", "email"), "\n")

        print("Repository Path : ", auth.repo_path, "\n\n")
        status_check()

    # Check Current branch. Enter "<branch_name>" to create new branch. ('<flag>', "<branch_name>")
        branch_chk = repo.git.branch('-a')

    # print(repo.git.branch())

        print("###### LIST OF BRANCH ######")
        print(branch_chk)
        print("############################\n\n")
    # print(type(branch_chk))

        #switch_branch = input("Do you want to switch branches (Yes or No): ").lower()
        #switch_branch = decouple.config('Switch_Branch')
        switch_branch = auth.switch_branch

        if switch_branch == 'yes':
            try:
                #branch_name = input("Which branch listed above that you would like to checkout: ").lower()
                #branch_name = decouple.config('branch_name')
                checkout = repo.git.checkout(auth.branch_name)
                branch = repo.git.branch()
                x = branch.splitlines()
                #print(x)

                for string in x:
                    if string[0] == '*':
                        # print("######## PRINT BRANCH currently checked out#########")
                        print("The branch currently checked out is: ", string[2:])
            except git.exc.GitError as GitError:
                print("Error: ", GitError)
            except:
                print("\nScript Abruptly Ended")
        else:
            branch = repo.git.branch()
            x = branch.splitlines()

            for string in x:
                if string[0] == '*':
                    # print("######## ELSE #########")
                    print("The branch which you will be committing to is: ", string[2:])
    except git.exc.GitError as GitError:
        print("Error: ", GitError)


def bare_checks():
    try:
        repo = git.Repo(auth.repo_path)
        print("Your BARE Repository is in : ", auth.repo_path)
    except git.exc.GitError as GitError:
        print("Error: ", GitError)


#non_bare_checks()
#status_check()
#bare_checks()