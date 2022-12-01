# Formatting Strings

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
# The output of this is "Hello Manny, your lucky number is 15"

# You can also write this another way like so

print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
# The output of this would be "Your lucky number is 15, Manny."

# Try this exorcise 
#
# Modify the student_grade function using the format method, 
# so that it returns the phrase "X received Y% on the exam". 
# For example, student_grade("Reed", 80) should return "Reed 
# received 80% on the exam".

def student_grade(name, grade):
	return ""

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# The correct way to write this is like so

def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
# The output of this looks like this
#
# Reed received 80% on the exam
# Paige received 92% on the exam
# Jesse received 85% on the exam