# Understanding While Loops
#
# What is a while loop?
#
# While loops instruct your computer to continuously execute your code
# based on the value of a condition. This is similar to 'if' statements
# the only difference is the body of the code can execute multiple times
# instead of just once 


# Example

x = 0                                      # Here you are assigning the value '0' to the variable 'x' this is called "Initializing" (To give an initial value to a variable)
while x < 5:                               # Here you are setting a condition for the 'while loop' that the variable 'x' needs to be smaller than '5' the condition is true becausee we know that 'x' is smaller than '0'
    print("Not there yet, x=" + str(x))    # Line 15 and 16 is the body of the 'while loop'.
    x = x + 1                              # Here is were you increment the value of 'x' by adding '1' and assigning it back to 'x'. There for at the execution of 'x' it will be 1 instead of 0 (x = 1)
print("x=" + str(x))


# Run this code and the output should be as follows:
# 
# Not there yet, x= 0
# Not there yet, x= 1
# Not there yet, x= 2
# Not there yet, x= 3
# Not there yet, x= 4
# x=5

# Once the condition reaches the value set in Line 14 the conddition is 'false' and the loop will stop running

# Read more below


# The Anatomy of a 'While Loop'
#
# A while loop will continuously execute code depending on the value of a condition. 
# It begins with the keyword while, followed by a comparison to be evaluated, then a colon. 
# On the next line is the code block to be executed, indented to the right. 
# Similar to an if statement, the code in the body will only be executed if the 
# comparison is evaluated to be true. What sets a while loop apart, however, is that this 
# code block will keep executing as long as the evaluation statement is true. Once the statement 
# is no longer true, the loop exits and the next line of code will be executed.  