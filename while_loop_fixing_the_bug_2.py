# The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# This is the fix to the above problem (Keep in mind that some loops are good like the "Ping" command)

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
    n += 1 # Adding this line helps to keep it from looping to long or from and infinite loop
		
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 