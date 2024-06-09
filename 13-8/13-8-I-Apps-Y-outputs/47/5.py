
def get_minimum_string(string, k):
    n = len(string)
    # Base case: if we can't perform any moves, return the original string
    if k == 0:
        return string
    
    # Initialize the minimum string to the original string
    minimum_string = string
    
    # Loop through each index in the string
    for i in range(n - 1):
        # If the current index is 1 and the next index is 0, we can swap them
        if string[i] == "1" and string[i + 1] == "0":
            # Swap the characters at indices i and i + 1
            minimum_string = minimum_string[:i] + "0" + minimum_string[i + 1] + "1" + minimum_string[i + 2:]
            # Decrement k by 1 since we used 1 move
            k -= 1
            # If k is now 0, we can't perform any more moves so return the minimum string
            if k == 0:
                return minimum_string
    
    # If we reach this point, we have performed all possible moves but the string is not sorted
    # So we return the sorted string
    return sorted(minimum_string)

