
def optimize_simulation_energies(n, m, k):
    # Initialize the simulation energies as the midpoint of each bin
    E = [i + 0.5 for i in range(n)]
    
    # Loop through each bin and find the closest simulation energy
    for i in range(n):
        # Find the index of the closest simulation energy
        j = min(range(m), key=lambda x: abs(E[i] - E[x]))
        
        # Update the simulation energy for this bin
        E[i] = E[j]
    
    # Calculate the sum of the squared distances between the photon energies and their closest simulation energies
    sum_squared_distances = sum([k[i] * (i - E[i]) ** 2 for i in range(n)])
    
    return sum_squared_distances

