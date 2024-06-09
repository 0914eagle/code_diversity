
def solve(intersections, streets, start_time, end_time, mister_george_route):
    # Initialize a dictionary to store the time it takes to travel between intersections
    time_dict = {}
    for street in streets:
        time_dict[street[0]] = street[2]

    # Initialize a list to store the intersections on Mister George's route
    mister_george_route = [int(x) for x in mister_george_route.split()]

    # Initialize a set to store the intersections that are blocked by Mister George
    blocked_intersections = set()

    # Loop through Mister George's route and block the intersections
    for i in range(len(mister_george_route) - 1):
        intersection1 = mister_george_route[i]
        intersection2 = mister_george_route[i + 1]
        blocked_intersections.add(intersection1)
        blocked_intersections.add(intersection2)

    # Initialize a queue to store the intersections to visit
    queue = []

    # Enqueue the starting intersection
    queue.append(start_time)

    # Initialize a dictionary to store the shortest time to reach each intersection
    shortest_time = {start_time: 0}

    # Loop until the queue is empty
    while queue:
        # Dequeue the first intersection
        intersection = queue.pop(0)

        # If the intersection is not blocked by Mister George, calculate the shortest time to reach it
        if intersection not in blocked_intersections:
            # Get the time it takes to travel to the intersection
            time_to_intersection = time_dict[intersection]

            # If the intersection is not the end intersection, enqueue the next intersection
            if intersection != end_time:
                queue.append(intersection + 1)

            # Update the shortest time to reach the intersection
            shortest_time[intersection + 1] = shortest_time.get(intersection, 0) + time_to_intersection

    # Return the shortest time to reach the end intersection
    return shortest_time[end_time]

