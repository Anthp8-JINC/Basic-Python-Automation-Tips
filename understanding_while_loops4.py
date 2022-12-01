# While loops use the condition to check when to exit.

# The body of the while loop needs to make sure that the condition
# being checked will change. If it doesn't change, the loop may never
# finish and we get what's called an infinite loop, a loop that keeps
# executing and never stops.

# Here is an example of an infinite loop

while x % 2 == 0:
    x = x / 2

# You can't divide any number by 0. Try this with a calculator to see what I mean
#  

# This is an example of how a loop should work. 'x' needs to be different than '0'

if x != 0:
    while x % 2 == 0:       # You can now nest this while loop inside an 'if' statement so that the 'while' loop is executed when 'x' is not equal to '0'
        x = x / 2

# Alternatively you can add the condition directly to the loop using logical operators like in the example below

while x != 0 and x % 2 == 0:
    x = x / 2