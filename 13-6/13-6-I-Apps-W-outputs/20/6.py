
def find_seals(n, a):
    # Initialize the list of seals
    seals = []

    # Iterate over the seals
    for i in range(n):
        # Find the seal with the minimum energy
        min_energy = min(a)

        # Find the index of the seal with the minimum energy
        min_index = a.index(min_energy)

        # Add the seal to the list of seals
        seals.append(min_energy)

        # Remove the seal from the list of energies
        a.pop(min_index)

    return seals

