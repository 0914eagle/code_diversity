
def solve(n, star_systems, e, links):
    # Initialize variables
    human_system, alien_system = None, None
    min_uw_distance = float('inf')

    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # If the current pair of star systems is valid, calculate the UW distance
            if star_systems[i] == 'h' and star_systems[j] == 'a':
                uw_distance = calculate_uw_distance(i, j, links)
                if uw_distance < min_uw_distance:
                    min_uw_distance = uw_distance
                    human_system, alien_system = i, j

    # Return the minimum UW distance and the pair of star systems with the minimum distance
    return min_uw_distance, (human_system, alien_system)

def calculate_uw_distance(i, j, links):
    # Initialize variables
    gravity_sequence = []
    capacitance, potential, inductance = 0, 0, 0

    # Calculate the gravity sequence and the capacitance, potential, and inductance of the sequence
    for k in range(i, j):
        gravity_sequence.append(links[k][0])
        capacitance += links[k][0] + links[k][1]
        potential += links[k][0] - links[k][1]
        inductance += links[k][0] * links[k][1]
    gravity_sequence.append(links[j][1])

    # Calculate the UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))

    return uw_distance

