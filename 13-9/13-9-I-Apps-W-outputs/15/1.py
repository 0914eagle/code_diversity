
def solve(N, K, A, D):
    # Initialize the maximum energy
    max_energy = 0
    
    # Loop through each possible bond change
    for i in range(N):
        # Check if the bond can be changed
        if i != K:
            continue
        
        # Change the bond
        E[i] = i + 1
        
        # Calculate the total energy
        total_energy = 0
        for j in range(N):
            if E[j] == i + 1:
                total_energy += A[j]
        
        # Update the maximum energy
        max_energy = max(max_energy, total_energy)
    
    # Return the maximum energy
    return max_energy

