# What is recursion?

# Recursion is the repeated application of the same procedure to a smaller problem
# Like a russian nesting doll that has multiple dolls inside of it

# Recursion lets us tackle complex problems by reducing the problem tot a simpler one.

# In programming, recursion is a way of doing a repetitive task by having a function call itself.

# Example of a recursion function

def factorial(n):                       # Here you define a function called 'factorial'
    if n < 2:                           # At the beggining  of the function you have conditional block defining the base case where 'n' is smaller than '2'
        return 1                        # Which then returns the value '1'
    return n * factorial(n-1)           # After the 'base case' we have a line where the factorial function is calling itself with 'n-1'. This is called the recursive case.


