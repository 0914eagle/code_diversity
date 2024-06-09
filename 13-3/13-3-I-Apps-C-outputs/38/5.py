
def solve(n, g, d, e, links):
    # Initialize variables
    human_system = None
    alien_system = None
    min_uw_distance = float('inf')

    # Loop through each system
    for i in range(n):
        # If the system is human, set it as the human system
        if d[i] == 'h':
            human_system = i
        # If the system is alien, set it as the alien system
        elif d[i] == 'a':
            alien_system = i

    # If both the human and alien systems have been found, calculate the UW distance
    if human_system is not None and alien_system is not None:
        # Calculate the capacitance, potential, and inductance of the gravity values
        capacitance = g[human_system] + g[alien_system]
        potential = g[human_system] - g[alien_system]
        inductance = g[human_system] * g[alien_system]

        # Calculate the UW distance
        uw_distance = abs(potential * (capacitance * capacitance - inductance))

        # If the UW distance is less than the minimum, update the minimum
        if uw_distance < min_uw_distance:
            min_uw_distance = uw_distance

    # Return the minimum UW distance
    return min_uw_distance

