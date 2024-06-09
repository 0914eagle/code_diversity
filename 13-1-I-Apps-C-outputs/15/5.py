
def solve(n, gravity, direct_links):
    # Initialize the minimum UW distance to a large value
    min_distance = 1000000
    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # If the two star systems are not directly linked, skip this pair
            if (i, j) not in direct_links and (j, i) not in direct_links:
                continue
            # Calculate the UW distance for this pair of star systems
            distance = calculate_distance(gravity[i], gravity[j])
            # If the UW distance is less than the minimum distance, update the minimum distance
            if distance < min_distance:
                min_distance = distance
    # Return the minimum UW distance
    return min_distance

def calculate_distance(g1, g2):
    # Calculate the capacitance, potential, and inductance for the two star systems
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2
    # Calculate the UW distance
    distance = abs(potential * (capacitance * capacitance - inductance))
    # Return the UW distance
    return distance

# Test the solve function with some example input
n = 9
gravity = [377, 455, 180, 211, 134, 46, 111, 213, 17]
direct_links = [(1, 2), (1, 4), (1, 6), (2, 3), (2, 4), (2, 5), (3, 5), (4, 6), (4, 7), (4, 9), (5, 7), (5, 8), (6, 9), (7, 9), (7, 8)]
print(solve(n, gravity, direct_links))

