
def reconstruct_permutation(n, a, b):
    # Initialize a dictionary to store the counts of each color
    color_count = {}
    for i in range(n):
        color_count[i+1] = 0
    
    # Increment the count of each color in the first meteor outburst
    for i in a:
        color_count[i] += 1
    
    # Decrement the count of each color in the second meteor outburst
    for i in b:
        color_count[i] -= 1
    
    # Initialize the permutation with the colors that appear only once
    permutation = []
    for i in range(1, n+1):
        if color_count[i] == 1:
            permutation.append(i)
    
    # Add the remaining colors to the permutation
    for i in range(1, n+1):
        if i not in permutation:
            permutation.append(i)
    
    return permutation

