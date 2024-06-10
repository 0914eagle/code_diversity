
def get_routes(n, m, roads):
    # Initialize a dictionary to store the routes
    routes = {}
    
    # Iterate over each road
    for road in roads:
        # Get the start and end areas of the road
        start, end = road[0], road[1]
        
        # If the route between the start and end areas doesn't exist, create a new list
        if (start, end) not in routes:
            routes[(start, end)] = []
        
        # Add the road to the list of routes between the start and end areas
        routes[(start, end)].append(road)
    
    # Return the dictionary of routes
    return routes

def get_min_animals(n, m, roads, p, q):
    # Get the routes between the start and end areas
    routes = get_routes(n, m, roads)
    
    # Initialize a list to store the minimum number of animals for each route
    min_animals = []
    
    # Iterate over each route between the start and end areas
    for route in routes[(p, q)]:
        # Get the start and end areas of the route
        start, end = route[0], route[1]
        
        # If the route is a direct connection, add the number of animals in the start area
        if start == p and end == q:
            min_animals.append(a[start - 1])
        
        # If the route is not a direct connection, add the minimum number of animals in the route
        else:
            min_animals.append(min(a[start - 1], a[end - 1]))
    
    # Return the minimum number of animals for the route
    return min(min_animals)

def get_average_f(n, m, roads):
    # Initialize a sum to store the sum of f(p, q) for all pairs p, q
    sum_f = 0
    
    # Iterate over each pair of areas
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            # If p is not equal to q, calculate f(p, q) and add it to the sum
            if p != q:
                sum_f += get_min_animals(n, m, roads, p, q)
    
    # Return the average of f(p, q) for all pairs p, q
    return sum_f / (n * (n - 1))

def main():
    # Read the input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    roads = []
    for i in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    
    # Calculate the average of f(p, q) for all pairs p, q
    average_f = get_average_f(n, m, roads)
    
    # Print the average
    print(average_f)

if __name__ == '__main__':
    main()

