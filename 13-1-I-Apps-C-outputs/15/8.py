
def solve(n, gravity, type, links):
    # Initialize variables
    human_system, alien_system = None, None
    min_distance = float('inf')

    # Loop through each system
    for i in range(n):
        # If the system is human, set it as the human system
        if type[i] == 'h':
            human_system = i
        # If the system is alien, set it as the alien system
        elif type[i] == 'a':
            alien_system = i

    # If both the human and alien systems have been found, calculate the minimum distance
    if human_system is not None and alien_system is not None:
        # Calculate the capacitance, potential, and inductance of the gravity values
        capacitance = gravity[human_system] + gravity[alien_system]
        potential = gravity[human_system] - gravity[alien_system]
        inductance = gravity[human_system] * gravity[alien_system]

        # Calculate the minimum distance
        min_distance = abs(potential * (capacitance * capacitance - inductance))

    # Return the minimum distance
    return min_distance

