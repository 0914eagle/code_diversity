
def get_minimum_distance(planets):
    # Calculate the distance between each pair of planets
    distances = {}
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            distance = get_distance(planets[i], planets[j])
            distances[(i, j)] = distance

    # Use a priority queue to keep track of the next planet to visit
    import heapq
    queue = [(0, 0)]
    visited = set()
    total_distance = 0
    while queue:
        distance, planet = heapq.heappop(queue)
        if planet in visited:
            continue
        visited.add(planet)
        total_distance += distance
        for neighbor in get_neighbors(planets, planet):
            if neighbor not in visited:
                heapq.heappush(queue, (distances[(planet, neighbor)], neighbor))

    return total_distance

def get_distance(planet1, planet2):
    return ((planet1[0] - planet2[0]) ** 2 + (planet1[1] - planet2[1]) ** 2 + (planet1[2] - planet2[2]) ** 2) ** 0.5

def get_neighbors(planets, planet):
    neighbors = []
    for i in range(len(planets)):
        if i != planet:
            neighbors.append(i)
    return neighbors

