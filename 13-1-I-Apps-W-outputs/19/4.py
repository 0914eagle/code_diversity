
def get_max_controlled_planets(num_planets, tunnels):
    # Initialize a graph with the given tunnels
    graph = [[] for _ in range(num_planets + 1)]
    for u, v in tunnels:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize an array to store the distances from each planet to the center planet (planet 1)
    distances = [0] * (num_planets + 1)
    
    # BFS to find the shortest distance from each planet to the center planet
    queue = [(1, 0)]
    while queue:
        planet, distance = queue.pop(0)
        if distances[planet] == 0:
            distances[planet] = distance
            for neighbor in graph[planet]:
                if distances[neighbor] == 0:
                    queue.append((neighbor, distance + 1))
    
    # Initialize an array to store the maximum number of controlled planets for each number of ships
    max_controlled_planets = [0] * (num_planets + 1)
    
    # Loop through each number of ships and find the maximum number of controlled planets
    for k in range(1, num_planets + 1):
        max_controlled_planets[k] = 1
        for planet in range(1, num_planets + 1):
            if distances[planet] <= k:
                max_controlled_planets[k] += 1
    
    return max_controlled_planets

