
def solve(m, n, p):
    # Initialize a dictionary to store the counts of each xor value
    xor_counts = {}
    
    # Iterate over the p sequence
    for i in range(len(p)):
        # Get the current xor value
        xor_value = p[i]
        
        # If the xor value is not in the dictionary, add it to the dictionary with a count of 1
        if xor_value not in xor_counts:
            xor_counts[xor_value] = 1
        # Otherwise, increment the count of the xor value
        else:
            xor_counts[xor_value] += 1
    
    # Initialize a variable to store the total number of sequences
    total_sequences = 1
    
    # Iterate over the xor values and their counts
    for xor_value, count in xor_counts.items():
        # Calculate the number of sequences for this xor value
        num_sequences = count ** n
        
        # Multiply the total number of sequences by the number of sequences for this xor value
        total_sequences *= num_sequences
        
        # Modulo the total number of sequences by 10^9+7 to avoid overflow
        total_sequences %= 1000000007
    
    # Return the total number of sequences
    return total_sequences
