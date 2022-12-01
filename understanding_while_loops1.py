# More 'While Loop' Examples

# This is a while loop inside of a function

def attempts(n):                            # Here you are defining the value 'n' to associate with the function 'attempts'
    x = 1                                   # Here you are assigning the value '1' to variable 'x'
    while x <= n:                           # Here you define that 'while' the varable 'x' is less than or equal to 'n'
        print("Attempt " + str(x))          # Here you tell should be done after the step above which is to print the word "Attemp " and "x" which is 1
        x += 1                              # Here you tell it to keep adding '1' until it reaches the invoking you set in line 12
    print("Done")                           # After it reaches the invoking you set in line 12 the word "Done" will be printed

attempts(5)

# The output should look like this

# Attempt 1
# Attempt 2
# Attempt 3
# Attempt 4
# Attempt 5
# Done