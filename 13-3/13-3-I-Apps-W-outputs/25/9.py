
def solve(N, T):
    # Initialize a variable to store the number of occurrences
    occurrences = 0
    
    # Loop through the concatenation of 10^10 copies of the string 110
    for i in range(10**10):
        # Check if the substring T occurs at the current position
        if T == "1011"[i:i+N]:
            # If it does, increment the number of occurrences
            occurrences += 1
    
    # Return the number of occurrences
    return occurrences

