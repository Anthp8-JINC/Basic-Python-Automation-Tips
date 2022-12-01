# Refactoring is where you make your code more
# presentable and easy to read

# Example

def calculated(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculated(5)

# The output is 78.5

# This is how the code looks after it is refactered 

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)

# The output is 78.5. This is a much cleaner look
