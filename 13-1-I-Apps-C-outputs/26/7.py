
def optimize_simulation_energies(n, m, k):
    # Initialize the simulation energies as the midpoint of each bin
    E = [i + 0.5 for i in range(n)]
    
    # Loop until the simulation energies converge
    while True:
        # Calculate the sum of the squared distances between the simulation energies and the true energies
        sum_squared_distances = 0
        for i in range(n):
            for j in range(m):
                sum_squared_distances += k[i] * (E[i] - E[j]) ** 2
        
        # If the sum of the squared distances is within the desired tolerance, return the simulation energies
        if sum_squared_distances < 1e-4:
            return E
        
        # Otherwise, update the simulation energies by moving them towards the true energies
        for i in range(n):
            E[i] = (1 - 0.1) * E[i] + 0.1 * (i + 0.5)

