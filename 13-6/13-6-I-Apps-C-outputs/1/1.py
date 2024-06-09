
def get_cost(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum cost of a path from the first building to the last building that avoids insecure buildings
    cost = float('inf')
    for i in range(n):
        if i + 1 not in insecure_buildings:
            cost = min(cost, dfs(graph, i, n - 1, insecure_buildings, 0))

    return cost if cost < float('inf') else -1

def dfs(graph, start, end, insecure_buildings, cost):
    if start == end:
        return cost

    for neighbor, weight in graph[start]:
        if neighbor not in insecure_buildings:
            new_cost = cost + weight
            dfs(graph, neighbor, end, insecure_buildings, new_cost)

    return cost

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    print(get_cost(n, m, p, insecure_buildings, connections))

if __name__ == '__main__':
    main()

