def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")

hint_username("an") # This will print "Invalid username"
hint_username("Anthony") #This will print "Valid username"