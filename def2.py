def area_triangle(base, height):
    return base*height/2

# Calculate the areas seporatly 
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

# The output should read " 20.5 "
