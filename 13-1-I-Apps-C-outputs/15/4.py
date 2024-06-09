
def solve(n, g, d, e, links):
    # Initialize variables
    human_systems = []
    alien_systems = []
    gravity_values = []
    capacitance = []
    potential = []
    inductance = []
    uw_distance = 0

    # Separate human and alien systems
    for i in range(n):
        if d[i] == "h":
            human_systems.append(i)
        else:
            alien_systems.append(i)

    # Calculate gravity values
    for i in range(n):
        gravity_values.append(g[i])

    # Calculate capacitance, potential, and inductance
    for i in range(n):
        capacitance.append(gravity_values[i] + gravity_values[i-1])
        potential.append(gravity_values[i] - gravity_values[i-1])
        inductance.append(gravity_values[i] * gravity_values[i-1])

    # Calculate UW distance
    for i in range(n):
        for j in range(n):
            if i != j:
                uw_distance += abs(potential[i] * (capacitance[i] * capacitance[j] - inductance[i] * inductance[j]))

    return uw_distance

