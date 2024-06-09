
def solve(f, b):
    n = len(f)
    m = len(b)
    if n != m:
        return "Impossible"
    
    # Create a dictionary to map each element of f to its index
    f_dict = {f[i]: i for i in range(n)}
    
    # Initialize a list to store the indices of b
    indices = [0] * m
    
    # Iterate through b and map each element to its index
    for i in range(m):
        indices[i] = f_dict[b[i]]
    
    # Check if there are any duplicates in indices
    if len(set(indices)) != m:
        return "Ambiguity"
    
    # If there are no duplicates, return the indices as the solution
    return "Possible\n" + " ".join(str(i + 1) for i in indices)

