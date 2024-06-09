
def solve(n, m):
    # Initialize a set to store the unique digits
    unique_digits = set()
    
    # Iterate over each hour
    for hour in range(n):
        # Iterate over each minute
        for minute in range(m):
            # Convert the hour and minute to base 7
            hour_base7 = str(hour).encode("utf-8").hex()
            minute_base7 = str(minute).encode("utf-8").hex()
            
            # Check if the hour and minute have distinct digits
            if len(set(hour_base7)) == len(hour_base7) and len(set(minute_base7)) == len(minute_base7):
                # Add the hour and minute to the set of unique digits
                unique_digits.add(hour_base7)
                unique_digits.add(minute_base7)
    
    # Return the number of unique pairs
    return len(unique_digits)

