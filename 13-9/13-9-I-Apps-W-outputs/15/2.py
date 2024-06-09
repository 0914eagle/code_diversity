
def solve(N, K, A, D):
    # Initialize the maximum energy and the current energy
    max_energy = 0
    current_energy = 0
    
    # Loop through each atom and change the bond
    for i in range(N):
        # Check if the current atom is excited
        if A[i] > 0:
            # Add the energy given by the excited atom to the current energy
            current_energy += A[i]
        
        # Check if the current atom is the last atom
        if i == N-1:
            # Break the loop
            break
        
        # Change the bond of the current atom
        E[i] = i+1
        
        # Check if the current atom is now excited
        if A[i] > 0:
            # Add the energy given by the excited atom to the current energy
            current_energy += A[i]
        
        # Check if the current energy is greater than the maximum energy
        if current_energy > max_energy:
            # Update the maximum energy
            max_energy = current_energy
    
    # Return the maximum energy
    return max_energy

