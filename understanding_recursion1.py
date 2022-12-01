# Example Recursion

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)

# The output should be 

# Factorial called with 4
# Factorial called with 3
# Factorial called with 2
# Factorial called with 1
# Returning 1
# Returning 2 for factorial of 2
# Returning 6 for factorial of 3
# Returning 24 for factorial of 4