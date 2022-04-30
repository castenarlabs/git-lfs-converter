import os
import auth_prep as auth


def script_summary():
    try:
        os.chdir(auth.repo_path)
        print("###################################")
        print("###  LFS REPO CONVERSION SUMMARY  ###")
        print("#####################################")
        print("")
        print('\033[1m' + 'GIT Objects Count / Size Check:\033[0m')
        count_objects = os.popen("git count-objects -vH").read()
        print(count_objects, "\n")
        print('\033[1m' + 'Git Attributes LFS Patterns that were converted\033[0m')
        pattern_attributes = os.popen("git show $(git cat-file HEAD -p | grep tree | awk '{print $2}'):.gitattributes | grep 'merge=lfs'").read()
        print(pattern_attributes, "\n")

        print('\033[1m' + 'Total GIT LFS File Count:\033[0m', os.popen('git lfs ls-files --all | wc -l').read())

        print('\033[1m' + 'List top 5 Largest LFS File (Bytes):\033[0m')
        print(os.popen("git lfs ls-files --debug --all | grep -e 'filepath' -e 'size' | awk -F: '{ print $2 }' | awk '!(NR%2){print$0p}{p=$0}' | sort -nr | head -5").read())
    except os.error() as e:
        print("\u274c Error: ", e)
