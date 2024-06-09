
def solve(n, g, d, e, links):
    # Initialize variables
    alien_systems = []
    human_systems = []
    gravity_values = []
    capacitance = []
    potential = []
    inductance = []
    uw_distance = 0

    # Separate the alien and human systems
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

    # Calculate the UW distance for each direct link
    for link in links:
        uw_distance += abs(potential[link[0]-1] * (capacitance[link[0]-1] * capacitance[link[1]-1] - inductance[link[0]-1]))

    # Return the minimum UW distance
    return uw_distance
