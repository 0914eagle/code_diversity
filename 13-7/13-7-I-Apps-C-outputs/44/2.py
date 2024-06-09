
def solve(n, star_systems, e, links):
    # Initialize variables
    min_uw_distance = float('inf')
    human_system, alien_system = None, None

    # Iterate over all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the UW distance between the two star systems
            uw_distance = calculate_uw_distance(star_systems, i, j, links)

            # If the UW distance is less than the current minimum, update the minimum and the selected star systems
            if uw_distance < min_uw_distance:
                min_uw_distance = uw_distance
                human_system = i
                alien_system = j

    # Return the minimum UW distance and the selected star systems
    return min_uw_distance, human_system, alien_system

def calculate_uw_distance(star_systems, i, j, links):
    # Initialize variables
    capacitance, potential, inductance = 0, 0, 0
    gravity_values = []

    # Calculate the capacitance, potential, and inductance for the path between the two star systems
    for k in range(len(links)):
        if links[k][0] == i and links[k][1] == j:
            capacitance += star_systems[links[k][0]][0] + star_systems[links[k][1]][0]
            potential += star_systems[links[k][0]][0] - star_systems[links[k][1]][0]
            inductance += star_systems[links[k][0]][0] * star_systems[links[k][1]][0]
        elif links[k][0] == j and links[k][1] == i:
            capacitance += star_systems[links[k][0]][0] + star_systems[links[k][1]][0]
            potential += star_systems[links[k][0]][0] - star_systems[links[k][1]][0]
            inductance += star_systems[links[k][0]][0] * star_systems[links[k][1]][0]
        else:
            continue

    # Calculate the UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))

    # Return the UW distance
    return uw_distance

