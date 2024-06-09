
def solve(N, M, A, B, K, G, streets):
    # Initialize a dictionary to store the time it takes to traverse each street
    street_times = {}
    for street in streets:
        street_times[street[0]] = street[1]

    # Initialize a dictionary to store the time it takes to reach each intersection from the starting intersection
    intersection_times = {}
    intersection_times[A] = 0

    # Loop through each intersection in the route
    for i in range(G):
        current_intersection = streets[i][1]
        next_intersection = streets[i][2]
        time_to_traverse_street = street_times[current_intersection]
        time_to_reach_next_intersection = intersection_times[current_intersection] + time_to_traverse_street
        intersection_times[next_intersection] = time_to_reach_next_intersection

    # Calculate the time it takes to reach the destination intersection
    time_to_reach_destination = intersection_times[B]

    # Calculate the least amount of time Luka needs to make his delivery
    return time_to_reach_destination + K

