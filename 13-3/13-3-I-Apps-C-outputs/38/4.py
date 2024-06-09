
def solve(n, star_systems, e, links):
    # Initialize variables
    human_system, alien_system = None, None
    min_uw_distance = float('inf')

    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # If one of the systems is human and the other is alien, calculate the UW distance
            if star_systems[i] == 'h' and star_systems[j] == 'a':
                uw_distance = calculate_uw_distance(i, j, links)
                # If the UW distance is less than the current minimum, update the minimum and the chosen star systems
                if uw_distance < min_uw_distance:
                    min_uw_distance = uw_distance
                    human_system, alien_system = i, j
            elif star_systems[i] == 'a' and star_systems[j] == 'h':
                uw_distance = calculate_uw_distance(j, i, links)
                if uw_distance < min_uw_distance:
                    min_uw_distance = uw_distance
                    human_system, alien_system = j, i

    return min_uw_distance

def calculate_uw_distance(i, j, links):
    # Initialize variables
    gravity_sequence = [star_systems[i].gravity, star_systems[j].gravity]
    capacitance, potential, inductance = 0, 0, 0

    # Calculate the capacitance, potential, and inductance of the gravity sequence
    for k in range(1, len(gravity_sequence)):
        capacitance += gravity_sequence[k] + gravity_sequence[k-1]
        potential += gravity_sequence[k] - gravity_sequence[k-1]
        inductance += gravity_sequence[k] * gravity_sequence[k-1]

    # Calculate the UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))

    return uw_distance

# Test the function with the sample input
n = 9
star_systems = ['a', 'h', 'a', 'a', 'a', 'h', 'h', 'h', 'a']
e = 15
links = [(1, 2), (1, 4), (1, 6), (2, 3), (2, 4), (2, 5), (3, 5), (4, 6), (4, 7), (4, 9), (5, 7), (5, 8), (6, 9), (7, 9), (7, 8)]
print(solve(n, star_systems, e, links))

