
def solve(intersections, streets, start_time, end_time, route):
    # Initialize a dictionary to store the time it takes to reach each intersection
    time_dict = {}
    for intersection in intersections:
        time_dict[intersection] = 0

    # Iterate through the route and calculate the time it takes to reach each intersection
    for i in range(start_time, end_time):
        for street in streets:
            if street[0] == route[i-1] and street[1] != route[i]:
                time_dict[street[1]] = max(time_dict[street[1]], time_dict[street[0]] + street[2])

    # Return the minimum time it takes to reach the end intersection
    return min(time_dict.values())

