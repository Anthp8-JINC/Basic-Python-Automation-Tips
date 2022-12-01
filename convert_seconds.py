# The sign "//" is a floor division. It divids a number and takes the integer number as the result
# Example 5//2 wouldn't be 2.5 it would simply 2

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# The output for 5000 should be "1 23 20"