
def solve(N, K, A, D):
    # Initialize the maximum energy and the current energy
    max_energy = 0
    current_energy = 0
    
    # Loop through each atom and check if it can be excited
    for i in range(N):
        # Check if the atom is not already excited
        if A[i] > 0:
            # Check if the atom has enough energy to be excited
            if D[i] <= current_energy:
                # Excite the atom and add its energy to the current energy
                current_energy += A[i]
                # Update the maximum energy if necessary
                max_energy = max(max_energy, current_energy)
    
    # Return the maximum energy
    return max_energy

