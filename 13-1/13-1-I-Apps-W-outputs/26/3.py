
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
    
    # Initialize a dictionary to store the number of spaceships assigned to attack each base
    spaceship_assignment = {}
    for x in range(n):
        spaceship_assignment[x] = 0
    
    # Initialize a dictionary to store the number of dummy bases created
    dummy_base_count = {}
    for x in range(n):
        dummy_base_count[x] = 0
    
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop through each spacehip
    for spaceship in spaceships:
        # Get the location and attacking strength of the spaceship
        x, a = spaceship[0], spaceship[1]
        x = x-1
        
        # Loop through each base
        for y in range(n):
            # Check if the base is not already assigned to a spaceship
            if spaceship_assignment[y] == 0:
                # Check if the base is not a dummy base
                if y not in dummy_base_cost:
                    # Check if the spaceship can attack the base
                    if a >= base_cost[y]:
                        # Assign the spaceship to attack the base
                        spaceship_assignment[y] = x+1
                        break
    
    # Loop through each base
    for y in range(n):
        # Check if the base is not already assigned to a spaceship
        if spaceship_assignment[y] == 0:
            # Check if the base is not a dummy base
            if y not in dummy_base_cost:
                # Create a dummy base
                dummy_base_count[y] += 1
                dummy_base_cost[y] = h
    
    # Calculate the total cost
    total_cost = 0
    for x in range(n):
        total_cost += dummy_base_cost[x] * dummy_base_count[x]
    
    # Return the minimum cost
    return total_cost

if __name__ == '__main__':
    n, m = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(m)]
    s, b, k, h = map(int, input().split())
    spaceships = [list(map(int, input().split())) for _ in range(s)]
    bases = [list(map(int, input().split())) for _ in range(b)]
    print(get_min_gold_cost(n, m, s, b, k, h, spaceships, bases))

