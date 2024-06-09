
def solve(N, K, A, D):
    # Initialize the maximum energy and the current energy
    max_energy = 0
    current_energy = 0
    
    # Create a list to store the changed bonds
    changed_bonds = [False] * N
    
    # Loop through each atom
    for i in range(N):
        # If the atom is not excited and the current energy is less than the total energy needed to excite the atom,
        # then exciting the atom will not give any energy gain
        if not changed_bonds[i] and current_energy < D[i]:
            continue
        
        # Excite the atom and add the energy given by the atom to the current energy
        current_energy += A[i]
        
        # If the atom has a bond, then exciting the atom will also excite the bonded atom
        if i + 1 < N:
            current_energy += A[i + 1]
        
        # Add the energy given by the atom to the maximum energy
        max_energy += A[i]
        
        # Mark the bond as changed
        changed_bonds[i] = True
    
    # Return the maximum energy
    return max_energy

