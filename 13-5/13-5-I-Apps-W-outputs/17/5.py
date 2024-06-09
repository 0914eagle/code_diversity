
def get_min_cost(n, m, k, roads, storages):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop over all possible cities to open the bakery
    for b in range(1, n+1):
        # If the city has a storage, skip it
        if b in storages:
            continue
        
        # Loop over all possible storages
        for s in storages:
            # Get the cost of flour delivery from the storage to the bakery
            cost = get_cost(roads, s, b)
            
            # If the cost is less than the minimum cost, update the minimum cost
            if cost < min_cost:
                min_cost = cost
    
    # Return the minimum cost
    return min_cost

def get_cost(roads, s, b):
    # Initialize the cost to 0
    cost = 0
    
    # Loop over all roads between the storage and the bakery
    for road in roads:
        # If the road connects the storage and the bakery, add the length of the road to the cost
        if (road[0] == s and road[1] == b) or (road[0] == b and road[1] == s):
            cost += road[2]
    
    # Return the cost
    return cost

def main():
    # Read the input
    n, m, k = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    storages = list(map(int, input().split()))
    
    # Get the minimum cost
    min_cost = get_min_cost(n, m, k, roads, storages)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

