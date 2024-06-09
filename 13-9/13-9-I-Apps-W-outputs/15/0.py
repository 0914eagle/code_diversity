
def solve(N, K, A, D):
    # Initialize the maximum energy to 0
    max_energy = 0
    
    # Loop through each possible value for E_i
    for i in range(1, N+1):
        # Check if the current value of E_i is not equal to i
        if i != E_i:
            # Calculate the total energy gained by exciting atom i
            total_energy = sum(A[j] for j in range(1, N+1) if j != i and E_i == j+1)
            
            # Check if the total energy gained is greater than the maximum energy
            if total_energy > max_energy:
                # Update the maximum energy
                max_energy = total_energy
    
    # Return the maximum energy
    return max_energy

