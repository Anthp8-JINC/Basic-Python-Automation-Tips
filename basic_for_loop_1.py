values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
  sum += value
  length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))