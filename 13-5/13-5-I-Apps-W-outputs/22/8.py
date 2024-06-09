
def solve(n, permutation, sequence):
    # Initialize a count of the number of elements to change
    count = 0
    
    # Convert the permutation and sequence to lists
    permutation = list(permutation)
    sequence = list(sequence)
    
    # Iterate over each element in the permutation
    for i in range(n):
        # If the element is not in its correct position, increase the count
        if permutation[i] != i + 1:
            count += 1
        
        # If the element is in its correct position and the sequence is not 0, increase the count
        if permutation[i] == i + 1 and sequence[i] == 1:
            count += 1
    
    # Return the count
    return count

