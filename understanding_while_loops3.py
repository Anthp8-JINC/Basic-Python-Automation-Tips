# In this code, there's an initialization problem that's causing our function to behave incorrectly.
# Can you find the problem and fix it?

def count_down(start_number):
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)

# The problem with this function is that 'count_down' is defined incorrectly.
# By replacing 'count_down(start_number)' with 'count_down(current)' corrects the issue because the values are set in the body to 'current'
# See how this function should be written

def count_down(current):
    while (current > 0):        # This tells that 'current' in 'count_down(current)' is greater than 0 for the count down to reach codes below it
        print(current)          # This prints the count down starting from the code 'count_down(3)' so the first thing to print on the screen is 3 will subtract from there using the code '-= 1'
        current -= 1            # This sets the condition of how much to subtract from the count down code 'count_down(3)'
    print("Zero!")              # This prints "Zero!" after the conditions have been met by setting the '-= 1' for a count down from the initiation code 'count_down(3)'

count_down(3)                   # This initiates the count down from a starting point you specify. In this case it is set to (3)

# The output is as follows:

# 3
# 2
# 1
# Zero!