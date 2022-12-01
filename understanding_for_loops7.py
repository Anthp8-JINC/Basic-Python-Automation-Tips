# The validate_users function is used by the system to check if a 
# list of users is valid or invalid. A valid user is one that is at 
# least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. 
# When calling it like in this example, something is not right. Can you figure out what to fix?

def validate_users(users):
    for user in users:
        if is_valid(user):                  # is_valid 
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users("purplecat")


# Correct way to write this code:

def validate_users(users):                  # Takes list as parameter
    for user in users:                      # Iterates for users[0]: ["purplecat"]
        if len(user) > 3:                   # Checks to see if the characters are greater than 3
            print(user + " is valid")
    else:
        print(user + " is invalid")

validate_users(['purplecat'])               # This is turned into a list

# Your output should be

# purplecat is valid