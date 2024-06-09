
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    
    # Iterate through the list and find the indices where A and B appear
    indices_A = [i for i, x in enumerate(perm) if x == A]
    indices_B = [i for i, x in enumerate(perm) if x == B]
    
    # If there are no indices where A and B appear, return -1
    if not indices_A or not indices_B:
        return -1
    
    # Otherwise, swap the elements at the indices where A and B appear
    perm[indices_A[0]], perm[indices_B[0]] = perm[indices_B[0]], perm[indices_A[0]]
    
    return " ".join(map(str, perm))

