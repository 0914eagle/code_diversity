
def solve(intersections, streets, start_intersection, end_intersection, k):
    # Initialize a dictionary to store the distances from the start intersection
    distances = {start_intersection: 0}
    # Initialize a queue to perform BFS
    queue = [start_intersection]
    # Loop until the queue is empty
    while queue:
        # Get the current intersection from the queue
        intersection = queue.pop(0)
        # Loop through the streets connected to the current intersection
        for street in streets[intersection]:
            # Get the next intersection and the distance to travel
            next_intersection, distance = street
            # If the next intersection is not in the dictionary, add it to the queue
            if next_intersection not in distances:
                distances[next_intersection] = distances[intersection] + distance
                queue.append(next_intersection)
    # Return the distance from the start intersection to the end intersection
    return distances[end_intersection]

