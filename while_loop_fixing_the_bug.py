#Find the bug
#def count_down(start_number):
  #while (current > 0):
    #print(current)
    #current -= 1
  #print("Zero!")

#count_down(3)



# Edit bug to the correct format (Changed the word "Current" to the name of the function "start_number")
def count_down(start_number):
  while (start_number > 0):
    print(start_number)
    start_number -= 1
  print("Zero!")

count_down(3)