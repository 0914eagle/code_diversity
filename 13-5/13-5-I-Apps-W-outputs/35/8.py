
def solve(m, n, p):
    # Initialize a dictionary to store the count of each possible x sequence
    x_count = {}
    
    # Iterate over each possible x sequence
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Check if the current x sequence is valid
            if i != j and i != p[i-1] and j != p[i-1]:
                # Increment the count of the current x sequence
                if (i, j) in x_count:
                    x_count[(i, j)] += 1
                else:
                    x_count[(i, j)] = 1
    
    # Return the total number of possible x sequences
    return sum(x_count.values()) % 1000000007

