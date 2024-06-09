
def get_energy_conversion_efficiency(n, U, energies):
    # Sort the energies in increasing order
    energies.sort()

    # Initialize the maximum energy conversion efficiency
    max_eta = 0

    # Iterate over all possible states i, j, and k
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Check if the energy difference between states i and k is less than or equal to U
                if energies[k] - energies[i] <= U:
                    # Calculate the energy conversion efficiency
                    eta = (energies[k] - energies[j]) / (energies[k] - energies[i])

                    # Update the maximum energy conversion efficiency
                    max_eta = max(max_eta, eta)

    # Return the maximum energy conversion efficiency
    return max_eta

