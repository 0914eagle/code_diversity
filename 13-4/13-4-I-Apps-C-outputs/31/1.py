
def solve(n, g, d, e, links):
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
        if d[i] == "a":
            alien_systems.append(i)
        else:
            human_systems.append(i)

    # Calculate the gravity values for each system
    for i in range(n):
        gravity_values.append(g[i])

    # Calculate the capacitance, potential, and inductance for each system
    for i in range(n):
        capacitance.append(gravity_values[i] + gravity_values[i-1])
        potential.append(gravity_values[i] - gravity_values[i-1])
        inductance.append(gravity_values[i] * gravity_values[i-1])

    # Calculate the UW distance for each pair of systems
    for i in range(n):
        for j in range(n):
            if i != j:
                uw_distance += abs(potential[i] * (capacitance[i] * capacitance[j] - inductance[i]))

    # Return the minimum UW distance
    return uw_distance

