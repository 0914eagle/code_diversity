
def solve(N, K, A, D):
    # Initialize the maximum energy as 0
    max_energy = 0
    
    # Loop through each atom and its bond
    for i in range(N):
        for j in range(i+1, N):
            # If the bond is changed, update the maximum energy
            if i != j and D[i] + D[j] <= K:
                max_energy = max(max_energy, A[i] + A[j])
    
    # Return the maximum energy
    return max_energy

