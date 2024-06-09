
def get_min_gold_cost(n, m, s, b, k, h, spaceships, bases):
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
    
    # Loop through each spaceship and calculate the minimum cost of attacking a base
    for x, a, f in spaceships:
        min_cost = float('inf')
        for y in graph[x-1]:
            if base_cost[y] <= a and f >= y-x:
                min_cost = min(min_cost, base_cost[y])
        spaceship_count[x-1] += 1
        dummy_base_count[x-1] += 1
        base_cost[x-1] = min_cost
    
    # Loop through each base and calculate the minimum cost of creating a dummy base
    for x in range(n):
        if spaceship_count[x] == 0:
            dummy_base_cost[x] = h
    
    # Calculate the total cost of creating dummy bases
    total_dummy_base_cost = sum(dummy_base_cost.values())
    
    # Calculate the total cost of attacking bases
    total_base_cost = sum(base_cost.values())
    
    # Return the minimum cost
    return total_dummy_base_cost + total_base_cost

if __name__ == '__main__':
    n, m = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(m)]
    s, b, k, h = map(int, input().split())
    spaceships = [list(map(int, input().split())) for _ in range(s)]
    bases = [list(map(int, input().split())) for _ in range(b)]
    print(get_min_gold_cost(n, m, s, b, k, h, spaceships, bases))

