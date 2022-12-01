number = int(input("Enter a number: "))

count = 1
while count <= 10:
  product = number * count
  print(number, "*", count, "=", product)
  count = count + 1

# The output should be

# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# 6 * 6 = 36
# 6 * 7 = 42
# 6 * 8 = 48
# 6 * 9 = 54
# 6 * 10 = 60


# Here is the reverse
count = 10
while count >= 1:
  product = number * count
  print(number, "*", count, "=", product)
  count = count - 1

# The output should be

# 6 * 10 = 60
# 6 * 9 = 54
# 6 * 8 = 48
# 6 * 7 = 42
# 6 * 6 = 36
# 6 * 5 = 30
# 6 * 4 = 24
# 6 * 3 = 18
# 6 * 2 = 12
# 6 * 1 = 6
