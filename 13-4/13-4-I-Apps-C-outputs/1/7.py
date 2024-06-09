
import itertools

def get_routes(n, m, roads):
    # Initialize a list to store the routes
    routes = []
    
    # Iterate over each possible starting point
    for start in range(1, n + 1):
        # Use itertools.permutations to generate all possible routes starting from the current start point
        for route in itertools.permutations(range(1, n + 1), n):
            # Check if the route is valid by checking if it visits each town exactly once and if it starts and ends at the correct towns
            if len(set(route)) == n and route[0] == start and route[-1] == 1:
                # Add the route to the list of routes
                routes.append(list(route))
    
    # Return the list of routes
    return routes

def count_routes(n, m, roads):
    # Initialize a set to store the unique routes
    unique_routes = set()
    
    # Iterate over each possible starting point
    for start in range(1, n + 1):
        # Use itertools.permutations to generate all possible routes starting from the current start point
        for route in itertools.permutations(range(1, n + 1), n):
            # Check if the route is valid by checking if it visits each town exactly once and if it starts and ends at the correct towns
            if len(set(route)) == n and route[0] == start and route[-1] == 1:
                # Add the route to the set of unique routes
                unique_routes.add(tuple(route))
    
    # Return the number of unique routes
    return len(unique_routes)

def main():
    # Read the input data
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Calculate the number of routes
    count = count_routes(n, m, roads)
    
    # Print the result
    print(count)

if __name__ == '__main__':
    main()

