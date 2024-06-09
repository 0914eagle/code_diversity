
def get_min_cost(n, m, s, b, k, h, spaceships, bases):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in m:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Initialize a dictionary to store the cost of attacking each base
    base_cost = {}
    for x, d in bases:
        base_cost[x-1] = d
    
    # Initialize a dictionary to store the cost of creating a dummy base
    dummy_base_cost = {}
    for x in range(n):
        dummy_base_cost[x] = h
    
    # Initialize a dictionary to store the number of spaceships attacking each base
    spaceship_count = {}
    for x in range(n):
        spaceship_count[x] = 0
    
    # Initialize a dictionary to store the number of dummy bases created
    dummy_base_count = {}
    for x in range(n):
        dummy_base_count[x] = 0
    
    # Loop through each spaceship and calculate the cost of attacking each base
    for x, a, f in spaceships:
        for y in graph[x-1]:
            if base_cost[y] <= a and f >= get_distance(x-1, y, graph):
                base_cost[y] -= k
                spaceship_count[y] += 1
    
    # Loop through each base and calculate the cost of creating a dummy base
    for x in range(n):
        if spaceship_count[x] == 0:
            dummy_base_cost[x] = 0
        else:
            dummy_base_count[x] += 1
    
    # Calculate the total cost of creating dummy bases
    total_cost = sum(dummy_base_cost.values())
    
    # Return the minimum cost
    return total_cost

def get_distance(x, y, graph):
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a queue to store the nodes to visit
    queue = [x]
    
    # Loop through the queue and visit each node
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == y:
                return len(visited) - 1
            queue.extend(graph[node])
    
    # If the destination is not reachable, return -1
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(m)]
    s, b, k, h = map(int, input().split())
    spaceships = [list(map(int, input().split())) for _ in range(s)]
    bases = [list(map(int, input().split())) for _ in range(b)]
    print(get_min_cost(n, m, s, b, k, h, spaceships, bases))

