
def solve(n, m):
    # Initialize a set to store the unique pairs
    unique_pairs = set()
    
    # Iterate over each hour
    for hour in range(n):
        # Iterate over each minute
        for minute in range(m):
            # Convert the hour and minute to base 7
            hour_base7 = convert_to_base7(hour)
            minute_base7 = convert_to_base7(minute)
            
            # Check if the hour and minute are distinct
            if hour_base7 != minute_base7:
                # Add the pair to the set
                unique_pairs.add((hour, minute))
    
    # Return the length of the set
    return len(unique_pairs)

# Convert a number to base 7
def convert_to_base7(num):
    # Initialize the base 7 representation
    base7_rep = ""
    
    # While the number is not zero
    while num > 0:
        # Get the remainder
        rem = num % 7
        
        # Add the remainder to the base 7 representation
        base7_rep = str(rem) + base7_rep
        
        # Divide the number by 7
        num //= 7
    
    # Return the base 7 representation
    return base7_rep

