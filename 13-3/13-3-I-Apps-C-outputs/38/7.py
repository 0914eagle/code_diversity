
def solve(n, g, d, e, links):
    # Initialize the minimum UW distance to a large value
    min_uw_distance = 1000000
    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # If the two star systems are of different types (human and alien), continue
            if d[i] != d[j]:
                continue
            # Calculate the UW distance between the two star systems
            uw_distance = calculate_uw_distance(g[i], g[j], links)
            # If the UW distance is less than the minimum, update the minimum
            if uw_distance < min_uw_distance:
                min_uw_distance = uw_distance
    # Return the minimum UW distance
    return min_uw_distance

def calculate_uw_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance of the two star systems
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2
    # Initialize the UW distance to the potential times the capacitance
    uw_distance = potential * capacitance
    # Loop through all direct links between the two star systems
    for link in links:
        # If the link is not between the two star systems, continue
        if link[0] != g1 and link[1] != g2:
            continue
        # Calculate the capacitance, potential, and inductance of the link
        link_capacitance = link[0] + link[1]
        link_potential = link[0] - link[1]
        link_inductance = link[0] * link[1]
        # Update the UW distance with the potential times the capacitance of the link
        uw_distance += link_potential * link_capacitance
    # Return the absolute value of the UW distance
    return abs(uw_distance)

n = 9
g = [377, 455, 180, 211, 134, 46, 111, 213, 17]
d = ['a', 'h', 'a', 'a', 'a', 'h', 'h', 'h', 'a']
e = 15
links = [[1, 2], [1, 4], [1, 6], [2, 3], [2, 4], [2, 5], [3, 5], [4, 6], [4, 7], [4, 9], [5, 7], [5, 8], [6, 9], [7, 9], [7, 8]]

print(solve(n, g, d, e, links))

