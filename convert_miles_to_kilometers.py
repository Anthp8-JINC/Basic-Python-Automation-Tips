


# 1) Complete the function to return the result of the conversion

def convert_distance(miles, km):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	miles = 55
	return km


# 2) Convert my_trip_miles to kilometers by calling the function above

km = convert_distance(55, int(1.6))

# 3) Fill in the blank to print the result of the conversion

print("The distance in kilometers is " + str(km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result

print("The round-trip in kilometers is " + str(km*2))