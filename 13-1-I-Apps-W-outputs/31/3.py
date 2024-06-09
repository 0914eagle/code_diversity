
def solve(n, m, gnomes):
    # Initialize a list to store the original sequence of gnomes
    original_sequence = []
    
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # If the current number is in the remaining gnomes, add it to the original sequence
        if i in gnomes:
            original_sequence.append(i)
    
    # Return the original sequence
    return original_sequence

