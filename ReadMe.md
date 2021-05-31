# This program is to automate existing repo conversion to LFS
(i) Ensure to take backup of repository (either bare or normal clone and checkout all branches)
(i) Check about logging for all these commands
### **Start LFS Tracking**
1. Normal Clone a Repository (main.py)

1. Install LFS Add files to be tracked by LFS

1. Commit to the repository

1. Push to remote

### **Track LFS files**

1. Bare Clone the Repository (main.py)

1. Instead of using BFG we're using "git lfs migrate"
    * Use Options
        * Use : `--everything`
        * Use : `--import=""`

1. Run command to check if LFS files exists
    * `git lfs ls-files --long --size --all`
    * `git lfs status`  

1. Run Aggressive GC
    * `git reflog expire --expire=now --all && git gc --prune=now --aggressive`

1. Force push bare repo
    * `git push --force`
        * Give user the option

### **Sample .env file**

    # USE HTTPS OR SSH URL (Either ONE, Leave the latter empty)
    repo_url = "https://bitbucket.org/castenar/jenkins-test.git"
    
    # LOCAL PATHS of where the cloned repository will be (/Users/pravin/Documents/Python/TESTCLONE/)
    repo_path = "/Users/pravin/Documents/Python/TESTCLONE/"
    
    # CREDENTIALS (Only for HTTPS)
    username = "<username>"
    app_password = ""

    #Define patterns separated by comma (,)
    patterns=jpg,png,mp3

    # Switch Branch (yes or no). If Switch Branch is (yes), "branch_name" should be enabled
    Switch_Branch = no
    branch_name =


