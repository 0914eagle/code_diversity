
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
    
    # Loop through each spaceship
    for spaceship in spaceships:
        # Get the location and attacking strength of the spaceship
        x, a = spaceship[0], spaceship[1]
        x = x-1
        
        # Loop through each base
        for base in bases:
            # Get the location and defensive strength of the base
            y, d = base[0], base[1]
            y = y-1
            
            # Check if the spaceship can attack the base
            if a >= d and graph[x][y] <= spaceship[2]:
                # Increment the number of spaceships assigned to attack the base
                spaceship_assignment[y] += 1
                
                # Check if the base is already assigned to be attacked
                if spaceship_assignment[y] > 1:
                    # Create a dummy base to attack the base
                    dummy_base_count[y] += 1
                    min_cost = min(min_cost, dummy_base_cost[y] + base_cost[y])
                else:
                    # Assign the spaceship to attack the base
                    min_cost = min(min_cost, base_cost[y])
    
    # Loop through each base
    for base in bases:
        # Get the location and defensive strength of the base
        y, d = base[0], base[1]
        y = y-1
        
        # Check if the base is not already assigned to be attacked
        if spaceship_assignment[y] == 0:
            # Create a dummy base to attack the base
            dummy_base_count[y] += 1
            min_cost = min(min_cost, dummy_base_cost[y] + base_cost[y])
    
    # Return the minimum cost
    return min_cost

def main():
    n, m = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(m)]
    s, b, k, h = map(int, input().split())
    spaceships = [list(map(int, input().split())) for _ in range(s)]
    bases = [list(map(int, input().split())) for _ in range(b)]
    print(get_min_gold_cost(n, m, s, b, k, h, spaceships, bases))

if __name__ == '__main__':
    main()

