# This function compares two numbers and returns them in increasing order.

# Fill in the blanks, so the print statement displays the result of the function call in order.

# Hint: if a function returns multiple values, don't forget to store these values in multiple variables


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
number2, number1 = order_numbers(100, 99)
print(number2, number1)