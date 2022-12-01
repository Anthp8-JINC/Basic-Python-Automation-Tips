# Question 1: What is recursion used for?

# Answer: Recursion lets us tackle complex problems by reducing the problem to a simpler one.

# Question 2: Which of these activities are good use cases for recursive programs?
    # 1. Going through a file system collecting information related to directories and files. (Correct)
    # 2. Creating a user account.
    # 3. Installing or upgrading software on the computer.
    # 4. Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users. (Correct)
    # 5. Checking if a computer is connected to the local network.




# Question 3:

# Fill in the blanks:

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return __

  # Recursive case: keep dividing number by base.
  return is_power_of(__, ___)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# Correct Answer

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
  result = number//base
  # Recursive case: keep dividing number by base.
  return is_power_of(result, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# Question 4

# Fill in the blanks:

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


# Correct Answer:

def count_users(group):
    count = 0
    for member in get_members(group):
    #count += 1
        if is_group(member):
            count += count_users(member)
        else:
            count+=1
    return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


# Question 5:

# Fill in the blanks:

def sum_positive_numbers(n):
  return 0

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


# Correct Answer:

def sum_positive_numbers(n):
    if n == 0:
        return n
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15