
def count_substring(T, N):
    # Initialize a variable to store the count
    count = 0
    
    # Loop through the string S
    for i in range(len(S) - N + 1):
        # Check if the substring T occurs at the current position
        if S[i:i+N] == T:
            # Increment the count
            count += 1
    
    # Return the count
    return count

