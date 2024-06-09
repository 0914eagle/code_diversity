
def solve(n, m):
    # Initialize a set to store the unique digits
    unique_digits = set()
    
    # Loop through each hour and minute combination
    for hour in range(n):
        for minute in range(m):
            # Convert the hour and minute to base 7
            hour_base7 = convert_to_base7(hour)
            minute_base7 = convert_to_base7(minute)
            
            # Check if the hour and minute have unique digits
            if len(set(hour_base7 + minute_base7)) == len(hour_base7) + len(minute_base7):
                unique_digits.add((hour, minute))
    
    # Return the number of unique pairs
    return len(unique_digits)

# Convert a number to base 7
def convert_to_base7(n):
    if n == 0:
        return "0"
    else:
        return convert_to_base7(n // 7) + str(n % 7)

