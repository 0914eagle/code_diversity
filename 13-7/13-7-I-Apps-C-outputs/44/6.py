
def solve(n, g, d, e, links):
    # Initialize variables
    human_systems = []
    alien_systems = []
    gravity_values = []
    capacitance = 0
    potential = 0
    inductance = 0
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
    for i in range(n-1):
        capacitance += gravity_values[i+1] + gravity_values[i]
        potential += gravity_values[i+1] - gravity_values[i]
        inductance += gravity_values[i+1] * gravity_values[i]

    # Calculate UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))

    return uw_distance

