
def solve(n, systems, e, links):
    # Initialize variables
    alien_systems = []
    human_systems = []
    gravity_values = []
    capacitance = []
    potential = []
    inductance = []
    uw_distance = 0

    # Separate the systems into alien and human systems
    for i in range(n):
        if systems[i] == "a":
            alien_systems.append(i)
        elif systems[i] == "h":
            human_systems.append(i)

    # Calculate the gravity values for each system
    for i in range(n):
        gravity_values.append(int(gravity_values[i]))

    # Calculate the capacitance, potential, and inductance for each system
    for i in range(n):
        capacitance.append(gravity_values[i] + gravity_values[i-1])
        potential.append(gravity_values[i] - gravity_values[i-1])
        inductance.append(gravity_values[i] * gravity_values[i-1])

    # Calculate the UW distance for each possible link between an alien and human system
    for alien_system in alien_systems:
        for human_system in human_systems:
            uw_distance += abs(potential[alien_system] * (capacitance[alien_system] * capacitance[human_system] - inductance[alien_system]))

    return uw_distance

