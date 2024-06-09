
def get_cost(connections, insecure_buildings):
    # Initialize the cost of the network to infinity
    cost = float('inf')
    
    # Iterate over all possible paths between buildings
    for path in itertools.permutations(range(1, n + 1)):
        # Check if the path satisfies the security measure
        if is_secure_path(path, insecure_buildings):
            # Calculate the cost of the path
            path_cost = sum(connections[i - 1][j - 1] for i, j in zip(path, path[1:]))
            # Update the cost of the network if the path is cheaper
            cost = min(cost, path_cost)
    
    return cost

def is_secure_path(path, insecure_buildings):
    # Check if the path passes through any insecure building
    for i in range(1, len(path)):
        if path[i] in insecure_buildings and path[i - 1] != path[i]:
            return False
    return True

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append([cost])
    
    print(get_cost(connections, insecure_buildings))

