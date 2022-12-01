# First Method
def hint_username(username):
    if len(username) < 3: # First (if) statment
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15: # Second (else) statment
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")




# Second Method (Much Cleaner)

def hint_username(username):
    if len(username) < 3: # First if statment
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15: #Second elif statment
        print("Invalid username. Must be at least 15 characters long")
    else:
        print("Valid username")