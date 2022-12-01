# The following code causes an infinite loop. Can you figure out what's missing and how to fix it?

def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)

print_range(1, 5) # This should print 1 2 3 4 5 (each number on its own line)

# The reason this will not happen is because we haven't set 'n' to plus or minus itself to anything
# We can do this by adding a line under 'print(n)' like 'n += 1'







# This is the correct way to write this code

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start                               # This is telling the function to start in 'print_range(start, end):' with the 'start' placeholder
	while n <= end:                         # Since 'n' is equal to 'start' letting the function know that it is '<=' to 'end' will tell it where to start when we invoke it with 'print_range(1, 5)'
		print(n)                            # This is telling the function to start at 'n' which equals 'start'
		n += 1                              # This is telling the function to increase by 1 using the '+='

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# Or the output should look like this

# 1
# 2
# 3
# 4
# 5

# Keep in mind that not all infinite loops are bad. Some are useful such as the ping utility.
# The command 'ping -t' will continuously run until an external action is met, like pressing 'CRTL-C'

# This is a code or program built into the terminal that when 'ping -t' is typed it can be canceled
# by pressing 'CRTL-C'