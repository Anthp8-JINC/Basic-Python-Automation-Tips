# This code loops a variable with a list

friends = ['Taylor', 'Alex', 'Pat', 'Eli']      # The variable 'friends' holds a list 'Taylor, Alex, Pat, Eli'
for friend in friends:                          # We give the 'for' function a value of 'friend' in 'friends' for the next line of code to print
    print("Hi " + friend)                       # We then tell the function to combine the above so the out put can be executed with 'print("Hi " + friend)

# The output should read

# Hi Taylor
# Hi Alex
# Hi Pat
# Hi Eli

# Another example (This code sums up all the numbers in the list and then gives you the average of those numbers)

values = [ 23, 52, 59, 37, 48 ]         # Here you are defining a list of 'values'
sum = 0                                 # Initializing variable 'sum' that will update in the body of the 'for' loop
length = 0                              # Initializing variable 'length' that will update in the body of the 'for' loop
for value in values:                    # The 'for' loop is iterating over each of the values in the list adding current value to the sum of values also adding 1 to length which will calculate how many elements there are in the list
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

# The output should read

# Total sum: 219 - Average: 43.8


