# Why Initializing Variables Matters

# This is an example of a function with no initialization

while my_variable < 10:
    print("Hello")
    my_variable += 1

# This is a bad function because the 'my_variable' isn't defined as anything
# You will receive the following error if you try to run this code

#ERROR: Traceback (most recent call last):
#           File "<stdin>", line 1, in <module>
#       NameError: name 'my_variable' is not defined

# To correct this code you will need to define the the 'my_variable'

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1

# The output will be the following:

# Hello
# Hello
# Hello
# Hello
# Hello

