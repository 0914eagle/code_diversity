
def solve(a, b, n, m, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Janet's house
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[n] = 0

    # Initialize a dictionary to store the previous intersection for each intersection
    previous = {i: None for i in range(1, n + 1)}

    # Loop through each road
    for u, v, t in roads:
        # If the current distance from intersection u to Janet's house is less than the current known distance, update the distance and previous intersection
        if distances[u] + t < distances[v]:
            distances[v] = distances[u] + t
            previous[v] = u

    # Initialize a set to store the intersections that have been visited
    visited = set()

    # Initialize a queue to store the intersections to visit
    queue = [n]

    # Loop through each intersection in the queue
    while queue:
        # Dequeue an intersection
        intersection = queue.pop(0)

        # If the intersection has been visited, skip it
        if intersection in visited:
            continue

        # Mark the intersection as visited
        visited.add(intersection)

        # If the intersection is not Janet's house, enqueue the previous intersection
        if intersection != 1:
            queue.append(previous[intersection])

    # Return the worst case waiting time
    return distances[1]

