
def solve(N, M, A, B, K, G, streets):
    # Initialize a dictionary to store the times at which each intersection is blocked
    blocked_times = {}

    # Loop through the list of streets
    for street in streets:
        # Get the start and end intersections of the street
        start, end = street[0], street[1]

        # If the start intersection is not already blocked, block it for the duration of the street
        if start not in blocked_times:
            blocked_times[start] = street[2]

        # If the end intersection is not already blocked, block it for the duration of the street
        if end not in blocked_times:
            blocked_times[end] = street[2]

    # Initialize a variable to store the least time needed to make the delivery
    least_time = 0

    # Loop through the list of intersections in Mister George's route
    for i in range(G):
        # Get the current intersection and the next intersection
        current, next = streets[i], streets[(i + 1) % G]

        # If the current intersection is blocked, add the blocked time to the least time needed to make the delivery
        if current in blocked_times:
            least_time += blocked_times[current]

        # If the next intersection is blocked, add the blocked time to the least time needed to make the delivery
        if next in blocked_times:
            least_time += blocked_times[next]

    # Return the least time needed to make the delivery
    return least_time

