
def get_max_efficiency(energies, upper_bound):
    n = len(energies)
    if n < 3:
        return -1
    max_efficiency = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if energies[k] - energies[i] <= upper_bound:
                    efficiency = (energies[k] - energies[j]) / (energies[k] - energies[i])
                    max_efficiency = max(max_efficiency, efficiency)
    return max_efficiency

