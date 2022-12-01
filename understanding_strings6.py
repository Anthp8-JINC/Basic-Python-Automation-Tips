# Let's say you want to output the price of an item 
# with and without tax. Depending on what the tax rate is, 
# the number might be a long number with a bunch of decimals. 
# So if something costs $7.5 without tax and the tax rate is 9%, 
# the price with tax would be $8.175.

price = 7.5
with_tax = price * 1.09
print(price, with_tax)      # Output is '7.5 8.175'

# You can print this another way to fix the issues

print("Base price: ${:.2f}. With Tax: ${:.2f}").format(price, with_tax))        # The output is 'Base price: $7.50. With Tax: $8.18'
# The '.2f' Means that you are formating a float number and there should be '2' decimal places after the '.' so no matter what the price is there will always be 2 decimal places


# Remember the celsius function?
# Using the formating function can make it look a lot nicer
# So instead of it looking this
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

# We can format it to look like this
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
# Out put is much cleaner

# 0 F   | -17.78 C
# 10 F  | -12.22 C
# 20 F  | -6.67 C
# 30 F  | -1.11 C
# 40 F  | -4.44 C
# 50 F  | -10.00 C
# 60 F  | -15.56 C
# 70 F  | -21.11 C
# 80 F  | -26.67 C
# 90 F  | -32.22 C
# 100 F | -37.78 C