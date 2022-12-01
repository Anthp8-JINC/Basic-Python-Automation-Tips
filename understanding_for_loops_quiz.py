# Question 1: How are while loops and for loops different in Python?
#
# Answer: While loops iterate while a condition is true, for loops iterate through a sequence of elements.



# Question 2: Fill in the blanks to make the factorial function return the factorial of n. 
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember 
# that the factorial of a number is defined as the product of an integer and all integers before it. 
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the 
# factorial of zero (0!) is equal to 1.

# Example

def factorial(n):
    result = 1
    for x in range(1,___):
        result = ___ * ___
    return ___

for n in range(___,___):
    print(n, factorial(n+___))



# Correct Way

def factorial(n):
    result = 1
    for x in range(2,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))

# The output is 

# Answer          # Figuring out the answer
# 0 1             # 0+1 = 1 # Carry the number after the '=' sign below to the next line
# 1 1             # 1+1 = 2
# 2 2             # 1+2 = 3
# 3 6             # 3*3 = 9
# 4 24            # 9*4 = 24
# 5 120           # 24*5 = 120
# 6 720           # 120*6 = 720
# 7 5040          # 720*7 = 5040
# 8 40320         # 5040*8 = 40320
# 9 362880        # 40320*9 = 362880


# Question 3: Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

# Example

for __ in range(__,__):
  print(__)

# Correct Way

for x in range(1,11):
 print(x*x*x)

 # Question 4: Write a script that prints the multiples of 7 between 0 and 100. 
 # Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
 # Remember that 0 is also a multiple of 7.

 # Example

 print()

 # Correct Way
multiple = range(0,100)
for num in multiple:
    if num%7==0:
        print(num)


# Question 5: The retry function tries to execute an operation that might fail, 
# it retries the operation for a number of attempts.  Currently the code will 
# keep executing the function even if it succeeds. Fill in the blank so the code 
# stops trying after the operation succeeded.

# Example

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
    ___
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)


# Correct Way

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break # will stop the loop when or if this is line reached
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)




