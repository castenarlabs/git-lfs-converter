import repo_clone  # from file repo_clone.py

bare = input("Do you want to Clone a bare repository (Enter Yes or No): ").lower()
while True:
    if bare == "yes":
        is_bare = True
        repo_clone.clone(is_bare)
        break
    elif bare == "no":
        is_bare = False
        repo_clone.clone(is_bare)
        break
    else:
        print("Please enter 'YES' OR 'NO': ")
        print(bare)
        bare = input("Do you want to Clone a bare repository (Enter Yes or No): ").lower()

# is_bare = False
# repo_clone.clone(is_bare)