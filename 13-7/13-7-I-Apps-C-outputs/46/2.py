
def get_insecure_buildings(n, p):
    insecure_buildings = set()
    for i in range(p):
        insecure_buildings.add(int(input()))
    return insecure_buildings

def get_direct_connections(m):
    direct_connections = []
    for i in range(m):
        x, y, cost = map(int, input().split())
        direct_connections.append((x, y, cost))
    return direct_connections

def find_cheapest_network(n, m, p, insecure_buildings, direct_connections):
    # Initialize the graph with the direct connections
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, cost in direct_connections:
        graph[x].add((y, cost))
        graph[y].add((x, cost))

    # Breadth-first search to find the shortest path between all pairs of buildings
    visited = set()
    queue = [(1, [])]
    while queue:
        current_building, path = queue.pop(0)
        if current_building not in visited:
            visited.add(current_building)
            for neighbor, cost in graph[current_building]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [cost]))

    # Check if the network satisfies the security measure
    for building in range(1, n + 1):
        if building in insecure_buildings:
            for neighbor, cost in graph[building]:
                if neighbor in insecure_buildings and building != neighbor:
                    return "impossible"

    # Return the cost of the cheapest network
    return min(sum(path) for path in visited)

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = get_insecure_buildings(n, p)
    direct_connections = get_direct_connections(m)
    print(find_cheapest_network(n, m, p, insecure_buildings, direct_connections))

if __name__ == '__main__':
    main()

