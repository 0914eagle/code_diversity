
def get_min_cost(n, m, k, roads, storages):
    # Initialize minimum cost to infinity
    min_cost = float('inf')
    
    # Loop over all cities that do not have storage
    for city in range(1, n + 1):
        if city not in storages:
            # Calculate the cost of opening the bakery in this city
            cost = calculate_cost(city, roads, storages)
            
            # If the cost is less than the minimum cost, update the minimum cost
            if cost < min_cost:
                min_cost = cost
    
    # Return the minimum cost
    return min_cost

def calculate_cost(city, roads, storages):
    # Initialize cost to 0
    cost = 0
    
    # Loop over all storages
    for storage in storages:
        # Calculate the distance between the bakery and the storage
        distance = get_distance(city, storage, roads)
        
        # Add the distance to the cost
        cost += distance
    
    # Return the cost
    return cost

def get_distance(city1, city2, roads):
    # Initialize distance to infinity
    distance = float('inf')
    
    # Loop over all roads between the two cities
    for road in roads:
        # If the road connects the two cities
        if (road[0] == city1 and road[1] == city2) or (road[0] == city2 and road[1] == city1):
            # Return the length of the road
            return road[2]
    
    # If no road connects the two cities, return infinity
    return distance

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    storages = set(map(int, input().split()))
    print(get_min_cost(n, m, k, roads, storages))

