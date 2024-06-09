
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
    for i in range(n-1):
        capacitance.append(gravity_values[i+1] + gravity_values[i])
        potential.append(gravity_values[i+1] - gravity_values[i])
        inductance.append(gravity_values[i+1] * gravity_values[i])

    # Calculate UW distance
    for i in range(e):
        uw_distance += abs(potential[links[i][0]-1] * (capacitance[links[i][0]-1] * capacitance[links[i][1]-1] - inductance[links[i][0]-1]))

    return uw_distance

