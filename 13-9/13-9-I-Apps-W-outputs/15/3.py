
def solve(N, K, A, D):
    # Initialize the maximum energy as 0
    max_energy = 0
    # Loop through each atom
    for i in range(N):
        # If the atom is not excited, continue to the next atom
        if A[i] == 0:
            continue
        # If the atom is excited, check if changing the bond is possible
        if K > 0:
            # Check if the bond can be changed
            if E[i] != i+1:
                # If the bond can be changed, change it to i+1
                E[i] = i+1
                # Decrement the number of bonds that need to be changed
                K -= 1
        # If the atom is excited and the bond can be changed, excite the atom
        if A[i] > 0:
            # Add the energy given by the atom to the maximum energy
            max_energy += A[i]
            # Set the energy given by the atom to 0
            A[i] = 0
    # Return the maximum energy
    return max_energy

