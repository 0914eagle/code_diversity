
def get_minimum_distance(planets):
    # Calculate the distance between each pair of planets
    distances = {}
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            distance = get_distance(planets[i], planets[j])
            distances[(i, j)] = distance

    # Use a priority queue to keep track of the planets to visit and their distances
    import heapq
    queue = [(0, 0, [])]
    visited = set()
    while queue:
        distance, current_distance, path = heapq.heappop(queue)
        if current_distance > distance:
            continue
        if len(path) == len(planets):
            return distance
        for i in range(len(planets)):
            if i in visited:
                continue
            visited.add(i)
            heapq.heappush(queue, (distance + distances[(path[-1], i)], current_distance + distances[(path[-1], i)], path + [i]))

    return -1

def get_distance(planet1, planet2):
    return ((planet1[0] - planet2[0]) ** 2 + (planet1[1] - planet2[1]) ** 2 + (planet1[2] - planet2[2]) ** 2) ** 0.5

