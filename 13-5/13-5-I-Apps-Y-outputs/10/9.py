
def solve(N, M, A, B, K, G, route, streets):
    # Initialize a dictionary to store the times at which each intersection is blocked
    blocked_times = {}

    # Loop through the streets that Mister George will visit
    for i in range(G):
        # Get the current and next intersection
        current_intersection = route[i]
        next_intersection = route[(i + 1) % G]

        # Get the time it takes to traverse the current street
        current_street = streets[current_intersection - 1][next_intersection - 1]

        # Add the current street to the blocked times dictionary
        blocked_times[current_intersection] = current_street

        # If the next intersection is not the last intersection, add the next street to the blocked times dictionary
        if i != G - 1:
            next_street = streets[next_intersection - 1][route[(i + 2) % G] - 1]
            blocked_times[next_intersection] = next_street

    # Initialize the least time needed to make the delivery
    least_time = 0

    # Loop through the streets between the starting intersection and the destination intersection
    for i in range(A - 1, B - 1):
        # If the current intersection is not blocked, add the time it takes to traverse the current street to the least time needed to make the delivery
        if i not in blocked_times or blocked_times[i] <= K:
            least_time += streets[i][i + 1]

    # Return the least time needed to make the delivery
    return least_time

