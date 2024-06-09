
def solve(self, N, K, A, D):
    # Initialize the maximum energy as 0
    max_energy = 0

    # Loop through each atom and calculate the maximum energy
    for i in range(N):
        # Calculate the total energy of the atom when it is excited
        total_energy = A[i]

        # Calculate the energy required to excite the atom
        energy_required = D[i]

        # Check if the atom can be excited
        if energy_required <= max_energy:
            # Excite the atom and calculate the total energy gained
            max_energy += total_energy

            # Decrease the energy required to excite the next atom
            energy_required -= total_energy

    # Return the maximum energy
    return max_energy

