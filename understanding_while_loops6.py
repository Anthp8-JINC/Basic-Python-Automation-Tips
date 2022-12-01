# This is an example of the terminal 'ping -t' utility code can be used for an infinite loop with a stop request

while True:                         # This condition can be set once you type 'ping -t' into the terminal
    do_something_cool()             # This is where the code for the 'ping -t' is doing what its meant to do when executed
    if user_requested_to_stop():    # This is where if you press the keys 'CRTL-C' the loop will stop the code 'ping -t' from executing    
        break                       # This signals that the current loop should stop running



# Infinite loops and Code Blocks

# Another easy mistake that can happen when using loops is introducing an infinite loop. 
# An infinite loop means the code block in the loop will continue to execute and never stop. 
# This can happen when the condition being evaluated in a while loop doesn't change. 
# Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.

# In the Coursera code blocks, you may see an error message that reads "Evaluation took more than 5 seconds to complete." 
# This means that the code encountered an infinite loop, and it timed out after 5 seconds. 
# You should take a closer look at the code and variables to spot where the infinite loop is.