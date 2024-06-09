
def get_divisible_by_3(s):
    # Initialize a counter for the number of divisible numbers
    count = 0
    
    # Iterate through the given number s
    for i in range(len(s)):
        # Check if the current digit is 3 or 6
        if s[i] in ["3", "6"]:
            # Increment the counter
            count += 1
    
    # Return the counter
    return count

