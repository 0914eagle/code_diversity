
def optimize_simulation_energies(n, m, k):
    # Initialize the simulation energies as the middle value of each bin
    E = [i + 0.5 for i in range(n)]
    
    # Loop through each bin and find the closest simulation energy
    for i in range(n):
        # Find the closest simulation energy to the current bin
        closest_energy = min(E, key=lambda x: abs(x - i))
        
        # Update the simulation energy for the current bin
        E[i] = closest_energy
    
    # Calculate the sum of the squared distances between the simulation energies and the actual energies
    sum_squared_distances = sum([k[i] * (E[i] - i) ** 2 for i in range(n)])
    
    return sum_squared_distances

