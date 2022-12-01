# More practice

def to_celsius(x):                  # First we are defining a function that converts a temperature value from fahrenheit to celsius using a conversion formula
    return (x-32)*5/9

for x in range(0,101,10):           # Then using a 'for' loop that starts at 0 going to 100 in increments of 10 (Notice that we use 101 for the upper limit instead of 100. This is because the 'range' never includes the last element and we want to include the number 100 in the range)
    print(x, to_celsius(x))         # This prints the answer in fahrenheit and celsius creating a conversion table


# The output should read:

# 0         -17.77777777777778
# 10        -12.222222222222221
# 20        -6.666666666666667
# 30        -1.1111111111111112
# 40        4.444444444444445
# 50        10.0
# 60        15.555555555555555
# 70        21.11111111111111
# 80        26.666666666666668
# 90        32.22222222222222
# 100       37.77777777777778


# Further explanation

# The range function can receive 1, 2 or 3 parameters

# The 1st parameter in this examples is '0'. 
# This generated a sequence of numbers from 0 to one less than we specified.
# The 1st parameter also specifies a starting point
# Ultimately - One perameter will create a sequence, one-by-one, from zero to one less than the parameter

# The 2nd parameter in this example is '101'.
# This generates a sequence that won't contain the last element and will stop one before the parameter specified. 
# Which is why we used 101 in this example.
# The 2nd parameter specifies an ending point.
# Ultimately - Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.

# The 3rd parameter lets you alter the size of each step.
# So instead of creating a sequence of numbers incremented by 1, 
# you can generate a sequence of numbers that incremented by 5 or in this example 10.
# Ultimately - Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.