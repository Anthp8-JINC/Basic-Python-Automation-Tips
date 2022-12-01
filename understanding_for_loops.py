# What is a for loop?

# A for loop iterates over a sequence of values

# An example of a for loop is how it can be used to iterate over a sequence of numbers

for x in range(5):
    print(x)

# The output of this should read

# 0
# 1
# 2
# 3
# 4

# The reason it shows this way is because when a computer counts it always starts with 0 unless you specify it not to
# by adding 'x += 1' in the line above 'print(x)'.

# Example:

for x in range(5):
    x += 1
    print(x) 

# The output should now read 

# 1
# 2
# 3
# 4
# 5