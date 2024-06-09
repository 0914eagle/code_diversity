
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
    
    # Iterate through all possible combinations of spaceships and dummy bases
    for spaceship_combination in itertools.combinations(range(s), r=b):
        # Initialize the cost of this combination to zero
        cost = 0
        
        # Iterate through each spaceship in the combination
        for spaceship in spaceship_combination:
            # Get the location of the spaceship
            x = spaceships[spaceship][0] - 1
            
            # Check if the spaceship has enough fuel to attack a base
            if spaceships[spaceship][2] >= graph[x][0]:
                # Get the cost of attacking the base
                cost += base_cost[graph[x][0]]
                
                # Increment the number of spaceships assigned to attack the base
                spaceship_assignment[graph[x][0]] += 1
            
            # Otherwise, create a dummy base
            else:
                # Get the cost of creating the dummy base
                cost += dummy_base_cost[x]
                
                # Increment the number of dummy bases created
                dummy_base_count[x] += 1
        
        # Check if the combination is valid
        if all(spaceship_assignment[x] <= 1 for x in range(n)) and all(dummy_base_count[x] <= 1 for x in range(n)):
            # Add the cost of this combination to the minimum cost
            min_cost = min(min_cost, cost)
    
    # Return the minimum cost
    return min_cost

if __name__ == '__main__':
    n, m = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(m)]
    s, b, k, h = map(int, input().split())
    spaceships = [list(map(int, input().split())) for _ in range(s)]
    bases = [list(map(int, input().split())) for _ in range(b)]
    print(get_min_gold_cost(n, m, s, b, k, h, spaceships, bases))

