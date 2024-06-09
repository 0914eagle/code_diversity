
import itertools

def get_routes(N, M, roads):
    # Initialize a list to store the routes
    routes = []
    
    # Iterate over each possible starting point
    for start in range(1, N + 1):
        # Use itertools.permutations to generate all possible routes starting from the current start point
        for route in itertools.permutations(range(1, N + 1), N):
            # Check if the route is valid by checking if all the roads are connected
            if all(roads[start][route[i]] for i in range(N)):
                # If the route is valid, add it to the list of routes
                routes.append(route)
    
    return len(routes)

def main():
    N, M = map(int, input().split())
    roads = {}
    for _ in range(M):
        a, b = map(int, input().split())
        if a not in roads:
            roads[a] = {}
        if b not in roads:
            roads[b] = {}
        roads[a][b] = roads[b][a] = True
    
    print(get_routes(N, M, roads))

if __name__ == '__main__':
    main()

