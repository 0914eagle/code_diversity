
def get_min_energy(n, q, a, k):
    # Initialize a dictionary to store the minimum energy released for each number of neutrons
    min_energy = {1: 0}

    # Loop through each number of neutrons from 2 to n
    for i in range(2, n + 1):
        # If the number of neutrons is less than or equal to the threshold, the minimum energy released is the amount of energy released when the atom is explodificated
        if i <= n:
            min_energy[i] = a[i - 1]
        # Otherwise, the minimum energy released is the maximum of the minimum energy released when the atom is decomposed into two sub-atoms
        else:
            # Find the largest number of neutrons that can be decomposed from the current number of neutrons
            j = i - n
            # Add the minimum energy released when the sub-atoms are explodificated to the minimum energy released when the current atom is explodificated
            min_energy[i] = max(min_energy[j], min_energy[i - j]) + a[n - 1]

    # Return the minimum energy released for the given number of neutrons
    return min_energy[k]

