
def solve(n, g, d, e, links):
    # Initialize variables
    human_systems = []
    alien_systems = []
    gravity_values = []
    capacitance = []
    potential = []
    inductance = []
    min_uw_distance = float('inf')

    # Separate human and alien systems
    for i in range(n):
        if d[i] == 'h':
            human_systems.append(i)
        else:
            alien_systems.append(i)

    # Calculate gravity values for each system
    for i in range(n):
        gravity_values.append(g[i])

    # Calculate capacitance, potential, and inductance for each system
    for i in range(n):
        capacitance.append(gravity_values[i] + gravity_values[i-1])
        potential.append(gravity_values[i] - gravity_values[i-1])
        inductance.append(gravity_values[i] * gravity_values[i-1])

    # Calculate UW distance for each pair of systems
    for i in human_systems:
        for j in alien_systems:
            uw_distance = abs(potential[i] * (capacitance[i] * capacitance[j] - inductance[i]))
            min_uw_distance = min(min_uw_distance, uw_distance)

    return min_uw_distance

