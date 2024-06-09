
def solve(intersections, streets, start_intersection, end_intersection, start_time_diff, route):
    # Initialize a dictionary to store the time it takes to travel between each pair of intersections
    time_dict = {}
    for street in streets:
        time_dict[(street[0], street[1])] = street[2]
        time_dict[(street[1], street[0])] = street[2]

    # Initialize a queue to store the intersections to visit
    queue = [start_intersection]

    # Initialize a set to keep track of the visited intersections
    visited = set()

    # Initialize the minimum time it takes to make the delivery
    min_time = float('inf')

    # Loop until the queue is empty
    while queue:
        # Get the current intersection
        intersection = queue.pop(0)

        # If the current intersection is the end intersection, calculate the time it takes to make the delivery and compare it with the minimum time
        if intersection == end_intersection:
            time = 0
            while queue:
                time += time_dict[queue[0], queue[1]]
                queue.pop(0)
            if time < min_time:
                min_time = time
            continue

        # If the current intersection has not been visited, mark it as visited and add its neighbors to the queue
        if intersection not in visited:
            visited.add(intersection)
            for neighbor in intersections[intersection]:
                queue.append(neighbor)

    # Return the minimum time it takes to make the delivery
    return min_time + start_time_diff

