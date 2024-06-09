
def longest_consecutive_subsequence(a, b):
    
    # Initialize the longest consecutive subsequence as 0
    lcs = 0

    # Iterate through the input sequence
    for i in range(len(a)):
        # Check if the current element is in the subset of integers
        if a[i] in b:
            # If the current element is in the subset, increment the longest consecutive subsequence
            lcs += 1
        else:
            # If the current element is not in the subset, break the loop
            break

    return lcs

