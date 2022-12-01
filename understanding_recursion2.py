# The function sum_positive_numbers should return the sum of all positive numbers 
# between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, 
# and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:

# Example

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return ___

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return ___ + sum_positive_numbers(___)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


# Correct Way using recursion
def sum_positive_numbers(n):
  if n <= 1:
      return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# Correct way using normal functions

def sum_positive_numbers(n):
  sums = 0
  for v in range(1,n+1):
    sums += v
  return sums

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

