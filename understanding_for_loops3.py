# In the previous section we used the 'range' function and how it generates a sequence of numbers starting with zero.
# Sometimes we may not want tot start with zero. For these situations, the 'range' function also allows us to specify 
# the first element of the list to generate.

# Example:

product = 1                     # We defined the value of 1 to the variable 'product'
for n in range (1, 10):         # We set 'n' for the 'range' of '1 through 10'
    product = product * n       # Then we redefined the variable 'product' which is 1 to multiply by 'n' which is the 'range' 1 through 10

print(product)                  # Wee then execute to print the answer of the variable 'product'

# Output should read

# 362880

# Better explanation

# We are calculating the product of all numbers from 1 to 10
# We start with 'product = 1' instead of 0 because if we used 0 the entire 'product' would equal out to 0





# Further example

# In math, the factorial of a number is defined as the product of an integer 
# and all the integers below it. For example, the factorial of four (4!) is 
# equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.

def factorial(n):
    result = 1
    for i in ___:
        ___
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120





# Correct way to write this code

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4)) # Should return the answer 24
print(factorial(5)) # Should return the answer 120