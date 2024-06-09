
def solve(n, m):
    # Initialize a set to store the unique digits
    unique_digits = set()
    
    # Iterate over each possible hour
    for hour in range(n):
        # Iterate over each possible minute
        for minute in range(m):
            # Convert the hour and minute to base 7
            hour_base7 = convert_to_base7(hour)
            minute_base7 = convert_to_base7(minute)
            
            # Check if the hour and minute have distinct digits
            if len(set(hour_base7 + minute_base7)) == len(hour_base7) + len(minute_base7):
                # Add the unique digits to the set
                unique_digits.update(hour_base7 + minute_base7)
    
    # Return the number of unique digits
    return len(unique_digits)

# Convert a number to base 7
def convert_to_base7(num):
    # Initialize the base 7 string
    base7_str = ""
    
    # Loop until the number is 0
    while num > 0:
        # Get the remainder
        remainder = num % 7
        
        # Add the remainder to the base 7 string
        base7_str = str(remainder) + base7_str
        
        # Divide the number by 7
        num //= 7
    
    # Return the base 7 string
    return base7_str

