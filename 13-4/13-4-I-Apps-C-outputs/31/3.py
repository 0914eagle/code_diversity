
def solve(n, g, d, e, links):
    # Initialize variables
    human_system = None
    alien_system = None
    min_distance = float('inf')

    # Loop through each system
    for i in range(n):
        # If the system is human, set it as the human system
        if d[i] == 'h':
            human_system = i
        # If the system is alien, set it as the alien system
        elif d[i] == 'a':
            alien_system = i

    # If both the human and alien systems have been found, calculate the distance between them
    if human_system is not None and alien_system is not None:
        # Calculate the capacitance, potential, and inductance of the path between the two systems
        capacitance = g[human_system] + g[alien_system]
        potential = g[human_system] - g[alien_system]
        inductance = g[human_system] * g[alien_system]

        # Calculate the UW distance
        distance = abs(potential * (capacitance * capacitance - inductance))

        # If the distance is less than the minimum distance, update the minimum distance
        if distance < min_distance:
            min_distance = distance

    # Return the minimum distance
    return min_distance

