
def get_cheapest_network(n, m, p, insecure_buildings, costs):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # Initialize the cost of the network to infinity
    network_cost = float('inf')
    
    # Iterate over all possible paths between the insecure buildings
    for path in itertools.permutations(insecure_buildings):
        # Calculate the cost of the path
        path_cost = 0
        for i in range(len(path) - 1):
            x, y = path[i], path[i + 1]
            path_cost += graph[x - 1][y - 1][1]
        
        # Update the network cost if the path cost is lower than the current cost
        if path_cost < network_cost:
            network_cost = path_cost
    
    # Return the network cost
    return network_cost

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for i in range(m):
        x, y, cost = map(int, input().split())
        costs.append((x, y, cost))
    print(get_cheapest_network(n, m, p, insecure_buildings, costs))

if __name__ == '__main__':
    main()

