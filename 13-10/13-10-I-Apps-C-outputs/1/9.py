
def read_input():
    N, M = map(int, input().split())
    roads = []
    for _ in range(M):
        O, D, L = map(int, input().split())
        roads.append((O, D, L))
    return N, M, roads

def get_shortest_path(N, M, roads):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(N + 1)]
    for O, D, L in roads:
        graph[O].append((D, L))
    
    # Initialize the distance of each city to infinity and the previous city to -1
    distance = [float('inf')] * (N + 1)
    previous = [-1] * (N + 1)
    distance[1] = 0
    
    # Relax all edges |V| - 1 times
    for _ in range(N - 1):
        for u in range(1, N + 1):
            for v, w in graph[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    previous[v] = u
    
    # Find the shortest path from city 1 to city N
    path = []
    u = N
    while previous[u] != -1:
        path.append(u)
        u = previous[u]
    path.append(1)
    path.reverse()
    
    # Return the shortest path
    return path

def get_shortest_paths(N, M, roads):
    # Get the shortest path from city 1 to city N
    path = get_shortest_path(N, M, roads)
    
    # Initialize the number of shortest paths containing each road to 0
    num_paths = [0] * M
    
    # Iterate through each road and increment the number of shortest paths containing it
    for i in range(M):
        O, D, L = roads[i]
        for j in range(len(path) - 1):
            if path[j] == O and path[j + 1] == D:
                num_paths[i] += 1
    
    # Return the number of shortest paths containing each road
    return num_paths

def main():
    N, M, roads = read_input()
    num_paths = get_shortest_paths(N, M, roads)
    for num in num_paths:
        print(num)

if __name__ == '__main__':
    main()

