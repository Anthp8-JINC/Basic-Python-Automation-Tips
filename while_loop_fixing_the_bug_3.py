# Fill in the blanks to make the print_prime_factors function print 
# all the prime factors of a number. A prime factor is a number that 
# is prime and divides another without a remainder.

#Bug Code
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = ___
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == ___:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      ___
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT











# Correct Code
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2 # Insert the number 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0: # Insert the number 0
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1 # Insert (factor += 1)
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT