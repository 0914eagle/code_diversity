
def solve(N, A, B):
    # Initialize a list to store the permutation
    permutation = list(range(1, N+1))
    
    # Iterate through the list and find the indices where A and B appear
    indices_A = [i for i, x in enumerate(permutation) if x == A]
    indices_B = [i for i, x in enumerate(permutation) if x == B]
    
    # If there are no indices where A and B appear, return -1
    if not indices_A or not indices_B:
        return -1
    
    # Swap the values at the indices where A and B appear to get the required permutation
    for i in indices_A:
        permutation[i] = B
    for i in indices_B:
        permutation[i] = A
    
    return permutation

