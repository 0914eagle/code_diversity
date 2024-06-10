
def get_cost(costs, insecure_buildings, n):
    # Initialize the graph with the given costs
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i].append((j, costs[i - 1][j - 1]))
    
    # Add the insecure buildings to the graph
    for building in insecure_buildings:
        for neighbor in range(1, n + 1):
            if neighbor != building:
                graph[building].append((neighbor, float('inf')))
    
    # Find the shortest path from each building to each other building
    distances = [float('inf')] * (n + 1)
    previous = [0] * (n + 1)
    queue = []
    queue.append(1)
    distances[1] = 0
    while queue:
        building = queue.pop(0)
        for neighbor, cost in graph[building]:
            if cost < distances[neighbor]:
                distances[neighbor] = cost
                previous[neighbor] = building
                queue.append(neighbor)
    
    # Calculate the total cost of the network
    total_cost = 0
    for i in range(1, n + 1):
        total_cost += distances[i]
    
    return total_cost

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for i in range(m):
        x, y, cost = map(int, input().split())
        costs.append([0] * (n + 1))
        costs[i][x] = cost
        costs[i][y] = cost
    
    total_cost = get_cost(costs, insecure_buildings, n)
    print(total_cost)

if __name__ == '__main__':
    main()

