
def solve(n, m):
    # Initialize a set to store all distinct pairs
    pairs = set()
    
    # Loop through all possible hours
    for hour in range(n):
        # Loop through all possible minutes
        for minute in range(m):
            # Convert hour and minute to base 7
            hour_base7 = convert_to_base7(hour)
            minute_base7 = convert_to_base7(minute)
            
            # If both hour and minute have distinct digits, add them to the set
            if has_distinct_digits(hour_base7) and has_distinct_digits(minute_base7):
                pairs.add((hour, minute))
    
    return len(pairs)

def convert_to_base7(num):
    # Convert the number to a string in base 7
    return str(num)

def has_distinct_digits(num_str):
    # Check if all digits in the number are distinct
    return len(set(num_str)) == len(num_str)

n, m = map(int, input().split())
print(solve(n, m))

