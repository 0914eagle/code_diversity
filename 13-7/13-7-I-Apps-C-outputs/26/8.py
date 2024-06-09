
def solve(N, A, B):
    # Initialize a list to store the permutation
    permutation = list(range(1, N+1))
    
    # Iterate through the list and find the indices where A and B appear
    indices_a = [i for i, x in enumerate(permutation) if x == A]
    indices_b = [i for i, x in enumerate(permutation) if x == B]
    
    # If there are no indices where A and B appear, return -1
    if not indices_a or not indices_b:
        return -1
    
    # Otherwise, swap the values at the indices where A and B appear
    permutation[indices_a[0]], permutation[indices_b[0]] = permutation[indices_b[0]], permutation[indices_a[0]]
    
    return permutation

