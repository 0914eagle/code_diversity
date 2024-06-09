
def find_max_efficiency(n, U, energies):
    # Initialize the maximum efficiency to 0
    max_efficiency = 0
    # Iterate over all possible states i, j, and k
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Check if the difference between the energies is less than or equal to U
                if energies[k] - energies[i] <= U:
                    # Calculate the energy conversion efficiency
                    efficiency = (energies[k] - energies[j]) / (energies[k] - energies[i])
                    # Update the maximum efficiency
                    max_efficiency = max(max_efficiency, efficiency)
    # Return the maximum efficiency
    return max_efficiency

