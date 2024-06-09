
def solve(N, A, B):
    # Initialize a list to store the permutation
    permutation = list(range(1, N+1))
    
    # Iterate through the list and calculate the value of g(i) for each i
    for i in range(1, N+1):
        # If g(i) is A, swap i with the first element of the list
        if g(permutation, i) == A:
            permutation[0], permutation[i-1] = permutation[i-1], permutation[0]
        # If g(i) is B, swap i with the last element of the list
        elif g(permutation, i) == B:
            permutation[-1], permutation[i-1] = permutation[i-1], permutation[-1]
    
    # If the list is not changed, it means that no such permutation exists
    if permutation == list(range(1, N+1)):
        return -1
    else:
        return permutation

def g(permutation, i):
    # If j is 1, return the value of P[i]
    if j == 1:
        return permutation[i-1]
    # Otherwise, calculate the value of f(P[i], j-1) and return it
    else:
        return g(permutation, permutation[i-1])

