
def get_min_speed(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for road in roads:
        graph[road[0]].add((road[1], road[2]))
    
    # Find the shortest path from the police car start to any exit
    shortest_path = []
    queue = [(start_police, 0)]
    visited = set()
    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current in exits:
                shortest_path = [current]
                break
            for neighbor, weight in graph[current]:
                queue.append((neighbor, distance + weight))
    
    # Find the shortest path from the brothers' start to the police car start
    brothers_path = []
    queue = [(start_brothers, 0)]
    visited = set()
    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current == start_police:
                brothers_path = [current]
                break
            for neighbor, weight in graph[current]:
                queue.append((neighbor, distance + weight))
    
    # Check if the brothers can reach the police car start before it reaches them
    if len(brothers_path) > len(shortest_path):
        return "IMPOSSIBLE"
    
    # Calculate the minimum speed required to escape
    min_speed = 0
    for i in range(len(brothers_path) - 1):
        min_speed += graph[brothers_path[i]][brothers_path[i + 1]][1]
    return min_speed

