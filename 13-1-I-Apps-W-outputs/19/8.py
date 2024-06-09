
def get_max_controlled_planets(num_planets, tunnels):
    # Initialize a graph with the given tunnels
    graph = [[] for _ in range(num_planets + 1)]
    for u, v in tunnels:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize an array to store the distances from each planet to the center planet (planet 1)
    distances = [0] * (num_planets + 1)
    
    # Breadth-first search from planet 1 to find the shortest distance to each other planet
    queue = [1]
    while queue:
        planet = queue.pop(0)
        for neighbor in graph[planet]:
            if distances[neighbor] == 0:
                distances[neighbor] = distances[planet] + 1
                queue.append(neighbor)
    
    # Return the maximum number of controlled planets for each K
    return [sum(1 for d in distances if d > 0) for _ in range(num_planets + 1)]

