
def solve(N, K, A, D):
    # Initialize the maximum energy to 0
    max_energy = 0
    # Loop through each atom i
    for i in range(N):
        # If the atom is not already excited
        if A[i] == 0:
            # Check if changing the bond of atom i to a different value than its current value will give a higher energy
            if D[i] + A[i] > max_energy:
                # Update the maximum energy
                max_energy = D[i] + A[i]
    return max_energy

