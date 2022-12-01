# Complete the function by filling in the missing parts. 
# The color_translator function receives the name of a color, 
# then prints its hexadecimal value. Currently, it only supports 
# the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

def exam_grade(score):
	if score >= 96:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail