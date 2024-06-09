
def reconstruct_permutation(n, a, b):
    # Initialize a dictionary to store the counts of each color
    color_count = {}
    for i in range(n):
        color_count[i+1] = 0
    
    # Increment the count of each color in the first meteor outburst
    for i in range(n):
        color_count[a[i]] += 1
    
    # Decrement the count of each color in the second meteor outburst
    for i in range(n):
        color_count[b[i]] -= 1
    
    # Initialize the permutation with the first color
    permutation = [1]
    
    # Add the remaining colors to the permutation
    for i in range(2, n+1):
        # Find the color with the highest count that is not already in the permutation
        for j in range(1, n+1):
            if color_count[j] > 0 and j not in permutation:
                permutation.append(j)
                color_count[j] -= 1
                break
    
    return permutation

