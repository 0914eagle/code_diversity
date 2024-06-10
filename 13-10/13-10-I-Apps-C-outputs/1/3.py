
def read_input():
    N, M = map(int, input().split())
    roads = []
    for _ in range(M):
        O, D, L = map(int, input().split())
        roads.append((O, D, L))
    return N, M, roads

def find_shortest_paths(N, M, roads):
    # Initialize the graph with the length of each road
    graph = {}
    for i in range(1, N+1):
        graph[i] = {}
    for O, D, L in roads:
        if D not in graph[O]:
            graph[O][D] = L
        else:
            graph[O][D] = min(graph[O][D], L)
    
    # Find the shortest paths from each city to each other city
    shortest_paths = {}
    for city in graph:
        shortest_paths[city] = {}
        for other_city in graph:
            if city == other_city:
                shortest_paths[city][other_city] = 0
            elif other_city in graph[city]:
                shortest_paths[city][other_city] = graph[city][other_city]
            else:
                shortest_paths[city][other_city] = float('inf')
    
    # Floyd-Warshall algorithm to find the shortest paths from each city to each other city
    for k in graph:
        for i in graph:
            for j in graph:
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])
    
    # Count the number of shortest paths containing each road
    road_count = [0] * M
    for O, D, L in roads:
        for i in range(1, N+1):
            if shortest_paths[O][D] == L:
                road_count[O-1] += 1
    
    return road_count

def main():
    N, M, roads = read_input()
    road_count = find_shortest_paths(N, M, roads)
    for count in road_count:
        print(count % 1000000007)

if __name__ == '__main__':
    main()

