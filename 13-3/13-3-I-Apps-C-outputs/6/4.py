
import itertools

def count_routes(n, m, roads):
    # Initialize a list to store the routes
    routes = []
    
    # Iterate over each possible route
    for route in itertools.permutations(range(1, n + 1)):
        # Check if the route is valid
        if is_valid_route(route, roads):
            # Add the route to the list
            routes.append(route)
    
    # Return the number of distinct routes
    return len(routes)

def is_valid_route(route, roads):
    # Initialize a set to store the visited towns
    visited = set()
    
    # Iterate over each town in the route
    for town in route:
        # Check if the town has already been visited
        if town in visited:
            # Return False if the town has already been visited
            return False
        # Add the town to the set of visited towns
        visited.add(town)
    
    # Return True if all towns have been visited
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    print(count_routes(n, m, roads))

