
def solve(n, m, remaining_gnomes):
    # Initialize a list to store the original sequence of gnomes
    original_sequence = [i for i in range(1, n+1)]
    
    # Sort the remaining gnomes in lexicographical order
    remaining_gnomes.sort()
    
    # Iterate through the remaining gnomes and find their indices in the original sequence
    for i in range(m):
        original_sequence[i] = remaining_gnomes[i]
    
    # Return the original sequence of gnomes
    return original_sequence

