
def solve(n, m):
    # Calculate the maximum number of places needed to display any integer from 0 to n-1
    max_hours = len(str(n-1))
    # Calculate the maximum number of places needed to display any integer from 0 to m-1
    max_minutes = len(str(m-1))
    # Initialize a set to store all unique pairs of hour and minute
    unique_pairs = set()
    # Iterate over all possible hours
    for hour in range(n):
        # Iterate over all possible minutes
        for minute in range(m):
            # Convert the hour and minute to strings in base 7
            hour_str = str(hour)
            minute_str = str(minute)
            # Add leading zeroes to the hour and minute strings if necessary
            if len(hour_str) < max_hours:
                hour_str = "0" * (max_hours - len(hour_str)) + hour_str
            if len(minute_str) < max_minutes:
                minute_str = "0" * (max_minutes - len(minute_str)) + minute_str
            # Add the pair of hour and minute to the set if it is not already present
            if (hour_str + minute_str) not in unique_pairs:
                unique_pairs.add(hour_str + minute_str)
    # Return the length of the set, which is the number of unique pairs of hour and minute
    return len(unique_pairs)

