
def read_input():
    N, M = map(int, input().split())
    roads = []
    for _ in range(M):
        O, D, L = map(int, input().split())
        roads.append((O, D, L))
    return N, M, roads

def shortest_paths(N, M, roads):
    # Initialize a dictionary to store the shortest paths from city 1 to each other city
    shortest_paths = {1: {1: 0}}
    for i in range(2, N+1):
        shortest_paths[i] = {i: 0}

    # Iterate through all the roads
    for O, D, L in roads:
        # If the road is from city O to city D, and the current shortest path from city 1 to city O is less than the length of the road, update the shortest path from city 1 to city O
        if O in shortest_paths and L < shortest_paths[O][O]:
            shortest_paths[O][O] = L

        # If the road is from city O to city D, and the current shortest path from city 1 to city D is less than the length of the road plus the current shortest path from city 1 to city O, update the shortest path from city 1 to city D
        if D in shortest_paths and L + shortest_paths[O][O] < shortest_paths[D][D]:
            shortest_paths[D][D] = L + shortest_paths[O][O]

        # If the road is from city O to city D, and the current shortest path from city 1 to city D is less than the length of the road plus the current shortest path from city 1 to city O, update the shortest path from city 1 to city D
        if D in shortest_paths and L + shortest_paths[O][O] < shortest_paths[D][D]:
            shortest_paths[D][D] = L + shortest_paths[O][O]

    # Count the number of shortest paths containing each road
    num_shortest_paths = [0] * M
    for i, (O, D, L) in enumerate(roads):
        if D in shortest_paths and L + shortest_paths[O][O] == shortest_paths[D][D]:
            num_shortest_paths[i] = 1

    return num_shortest_paths

def main():
    N, M, roads = read_input()
    num_shortest_paths = shortest_paths(N, M, roads)
    for num in num_shortest_paths:
        print(num)

if __name__ == '__main__':
    main()

