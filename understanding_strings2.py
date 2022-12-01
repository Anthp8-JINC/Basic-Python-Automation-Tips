# Creating New Strings

message = "A kong string with a silly typo"
new_message = message [0:2] + "l" + message[3:]     # This line fixes the error in the word "kong" above to "long"
print(new_message)


# This is a method to get an index of a certain character 
pets = "Cats & Dogs"
pets.index("&")         # The output is 5 because it is the 5th character in the string starting with position 0
pets.index("C")         # The output is 0 because it is the in position 0
pets.index("Dog")       # The output is 7 because it is the 7th character in the string starting with position 0
pets.index("s")         # The output is 3 because it is the 3rd character in the string starting with position 0
pets.index("x")         # The output would be an error because there is no character 'x'




# Find if a sub string is contained in a string
"Dragon" in pets # Returns (False) because Dragon isn't in the string "Cats & Dogs"
"Cats" in pets # Returns (True) because Cats is in thee string "Cats & Dogs"
