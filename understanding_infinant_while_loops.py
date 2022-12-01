# This is an example of a while loop that is infinant

count = 0

while count < 5:
    print("I am inside a loop.")
    print("Looping is interesting.")

# Both of the 'print' statements will print for ever because 'count' which is equal to '0' that is less than '5' is always true.
# So the condition will continue on forever

# To keep this from running forever you can add a statement that stops count like this

count = 0

while count < 5:
    print("I am inside a loop.")
    print("Looping is interesting.")
    count = count + 1                       # This is telling the 'while count < 5' to keep adding '1' until it reaches '5' (printing 5 times)
    