
def solve(m, n, p_sequence):
    # Initialize a dictionary to store the count of sequences
    # for each possible value of x_i
    counts = {}
    
    # Iterate over the p_sequence
    for p in p_sequence:
        # If this is the first occurrence of p, initialize the count to 1
        if p not in counts:
            counts[p] = 1
        # Otherwise, increment the count
        else:
            counts[p] += 1
    
    # Initialize the result to 0
    result = 0
    
    # Iterate over the counts dictionary
    for p, count in counts.items():
        # If the count is greater than 1, we can have at most (count - 1) sequences
        # with x_i = p, so we add (count - 1) to the result
        result += (count - 1)
    
    # Return the result modulo 10^9 + 7
    return result % 1000000007

