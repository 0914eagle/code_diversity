
def solve(N, K, A, D):
    # Initialize the maximum energy to 0
    max_energy = 0
    
    # Loop through each atom
    for i in range(N):
        # If the atom is not excited, continue to the next atom
        if A[i] == 0:
            continue
        
        # If the atom is excited, check if changing the bond is allowed
        if K > 0:
            # If changing the bond is allowed, change the bond to a different value
            E[i] = i + 1
            K -= 1
        
        # Add the energy given by the excited atom to the maximum energy
        max_energy += A[i]
    
    # Return the maximum energy
    return max_energy

