
def solve(n, systems, e, links):
    # Initialize the minimum UW distance
    min_uw_distance = float('inf')
    # Loop through all possible pairs of systems
    for i in range(n):
        for j in range(i+1, n):
            # If the systems are not directly linked, skip this pair
            if (i, j) not in links and (j, i) not in links:
                continue
            # Calculate the UW distance for this pair of systems
            uw_distance = calculate_uw_distance(systems, i, j)
            # Update the minimum UW distance
            min_uw_distance = min(min_uw_distance, uw_distance)
    # Return the minimum UW distance
    return min_uw_distance

def calculate_uw_distance(systems, i, j):
    # Initialize the UW distance
    uw_distance = 0
    # Loop through all the systems in the path between i and j
    for k in range(i, j):
        # Calculate the capacitance, potential, and inductance for this system
        capacitance = systems[k][0] + systems[k+1][0]
        potential = systems[k][0] - systems[k+1][0]
        inductance = systems[k][0] * systems[k+1][0]
        # Add the potential and inductance to the UW distance
        uw_distance += potential * (capacitance * capacitance - inductance)
    # Return the UW distance
    return abs(uw_distance)

