
def get_min_energy(n, q, a, k):
    # Initialize a dictionary to store the minimum energy released for each number of neutrons
    min_energy = {1: 0}

    # Loop through each query k
    for k in q:
        # If the atom has less than or equal to the neutron threshold, the minimum energy released is a[k]
        if k <= n:
            min_energy[k] = a[k]
        # Otherwise, the atom will decompose into two atoms with i and j neutrons respectively
        else:
            # Find the minimum energy released when the atom decomposes into two atoms with i and j neutrons
            min_energy[k] = min(min_energy[i] + min_energy[j] for i in range(1, k + 1) for j in range(1, k + 1) if i + j == k)

    # Return the minimum energy released for the query k
    return min_energy[k]

