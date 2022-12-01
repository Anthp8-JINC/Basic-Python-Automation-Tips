# This is an infinant loop. *DO NOT RUN THIS ON YOUR PC*
-while x % 2 == 0:
 - x = x /2

# This is a while loop used with an (if) function
# The while loop is executed only when x is NOT 0
if x != 0:
  while x % 2 == 0:
    x = x / 2

# You can use a logical operator to perform the condition instead of using the (if) function
while x != 0 and x % 2 == 0:
  x = x / 2