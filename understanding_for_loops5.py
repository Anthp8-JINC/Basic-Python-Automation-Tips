# Nested 'for' Loops (Loops inside of Loops)

# Dominoes is a good example of this

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

# The output should look like this

# [0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6] 
# [1|1] [1|2] [1|3] [1|4] [1|5] [1|6] 
# [2|2] [2|3] [2|4] [2|5] [2|6]
# [3|3] [3|4] [3|5] [3|6]
# [4|4] [4|5] [4|6]
# [5|5] [5|6]
# [6|6]


# Challenge: Find out how to write a code that will give this output

# [ 0 | 0 ]     [ 0 | 1 ]     [ 0 | 2 ]     [ 0 | 3 ]     [ 0 | 4 ]     [ 0 | 5 ]     [ 0 | 6 ]
# [ 1 | 0 ]     [ 1 | 1 ]     [ 1 | 2 ]     [ 1 | 3 ]     [ 1 | 4 ]     [ 1 | 5 ]     [ 1 | 6 ]
# [ 2 | 0 ]     [ 2 | 1 ]     [ 2 | 2 ]     [ 2 | 3 ]     [ 2 | 4 ]     [ 2 | 5 ]     [ 2 | 6 ]
# [ 3 | 0 ]     [ 3 | 1 ]     [ 3 | 2 ]     [ 3 | 3 ]     [ 3 | 4 ]     [ 3 | 5 ]     [ 3 | 6 ]
# [ 4 | 0 ]     [ 4 | 1 ]     [ 4 | 2 ]     [ 4 | 3 ]     [ 4 | 4 ]     [ 4 | 5 ]     [ 4 | 6 ]
# [ 5 | 0 ]     [ 5 | 1 ]     [ 5 | 2 ]     [ 5 | 3 ]     [ 5 | 4 ]     [ 5 | 5 ]     [ 5 | 6 ]
# [ 6 | 0 ]     [ 6 | 1 ]     [ 6 | 2 ]     [ 6 | 3 ]     [ 6 | 4 ]     [ 6 | 5 ]     [ 6 | 6 ]