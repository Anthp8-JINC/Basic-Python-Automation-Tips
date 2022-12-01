# More String Methods

"Mountains".upper() # This prints out 'MOUNTAINS' in all CAPS
"Mountains".lower() # This prints out 'mountains' in all Lower Case

# Check if a user answered "Yes" in all upper case or lower. You can transform the answer to the case you want.

answer = 'YES'
if answer.lower() == "yes"
    print("User said yes") # The output would be "User said yes"

# The strip method will get rid of surrounding spaces with in a string.

" yes ".strip()  # The output would be 'yes' with no spaces aka whitespace
" yes ".lstrip() # This removes the whitespace on the left side of the string so the output would be 'yes '
" yes ".rstrip() # This removes the whitespaces on the right side of the string so the output would be ' yes'

# The method 'count' returns how many times a given substring appears within a string.

"The number of times e occurs in this string is 4".count("e") # The output would be 4

# The  method 'endswith' returns whether the string ends with a certain substring.

"Forest".endswith("rest") # This returns a boolean value of 'True'


# The method 'isnumeric' returns wheather the string is made up of just number

"Forest".isnumeric()    # This returns a boolean value of 'True'
"12345".isnumeric()     # This returns a boolean value of 'False

# If you have a string that is numeric you can add the 'int' function to convert it into a number

int("12345") + int("54321")     # The output would be '66666'

# The 'join' method can be used for concatinating 

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]) # The out put would be "This is a phrase joined by spaces"

"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]) # Output "This...is...a...phrase...joined...by...triple...dots"


# The method 'split' splits a string into a list of strings

"This is another example".split() # Output is '['This', 'is', 'another', 'example']


# Here is a practice example
#
# Fill in the gaps in the initials function so that it returns the initials 
# of the words contained in the phrase received, in upper case. For example: 
# "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.___
    result = ""
    for word in words:
        result += ___
    return ___

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# The way to write this is

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        x=list(word)
        if x[0].isupper():
            result +=x[0]
        elif x[0].islower():
            result +=x[0].upper()
            
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS





