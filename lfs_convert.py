import repo_clone_push
import auth_prep as auth
import lfs_setup
import os
import decouple
from subprocess import PIPE, Popen


def pattern_handler():
    try:
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
    except Exception as e:
        print("\u274cUnable to construct pattern handler")
        print(e)


# pattern_handler()
# lfs_migrate = "git lfs migrate import --include='" + pattern_str + "' --everything"
# print(lfs_migrate)

def run_lfs_convert():
    # Pattern from .env file (pattern_handler func)
    pattern_handler()
    try:
        lfs_migrate = "git lfs migrate import --include='" + pattern_str + "' --everything"
        # bfg_command = "java -jar bfg.jar --convert-to-git-lfs '*.{" + pattern + "}' --no-blob-protection --private '" + auth.repo_path + "'"
        aggressive_gc = "git reflog expire --expire=now --all && git gc --prune=now --aggressive"
        # push_all = "git push --force --all && git lfs push origin --all"

        # Use LFS Migrate to convert files to LFS
        print("\n#####################################################")
        print("###  Converting to LFS with Git LFS Migrate Tool  ###")
        print("#####################################################")
        print("\n")
        print(" Files to convert matching pattern : ", pattern_str)
        # Change to repo directory
        os.chdir(auth.repo_path)
        print("\nRun Command :", lfs_migrate)

        # Used this for logging as actual output does into stderr
        lfs_cmd = Popen([lfs_migrate], stderr=PIPE, stdin=PIPE, shell=True, universal_newlines=True)
        output, error = lfs_cmd.communicate()
        print(error)
        print("\n")

        # Run Aggressive GC
        print("################################")
        print("###  RUNNING AGGRESSIVE GC  ###")
        print("################################")
        print("\n")
        print("\n Run Aggressive_gc: ", aggressive_gc)

        gc_1 = "git reflog expire --expire=now --all"
        gc_2 = "git gc --prune=now --aggressive"

        reflog = Popen([gc_1], stderr=PIPE, stdout=PIPE, shell=True, universal_newlines=True)
        out, err = reflog.communicate()

        reflog = Popen([gc_2], stderr=PIPE, stdout=PIPE, shell=True, universal_newlines=True)
        out, err = reflog.communicate()
        print(out, err)

    # agg_gc = Popen([gc_2], stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True, universal_newlines=True)
    # out2, err2 = agg_gc.communicate()
    # print(out2, err2)
    # print("\n")


        print("\n")

        # Force Push Repository and LFS files
        print("############################################")
        print("###  Force Push Repository & LFS Objects ###")
        print("############################################")
        print("\n")
        repo_clone_push.lfs_force_push()

        # Change back to lfs converter repo
        lfs_setup.chdir_to_pyrepo()
    except Exception as e:
        print("\u274cError: ", e)
