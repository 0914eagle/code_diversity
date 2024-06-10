
def get_input():
    N, M = map(int, input().split())
    roads = []
    for _ in range(M):
        O, D, L = map(int, input().split())
        roads.append((O, D, L))
    return N, M, roads

def find_shortest_paths(N, M, roads):
    # Initialize the shortest path matrix with infinite distances
    shortest_paths = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        shortest_paths[i][i] = 0

    # Fill in the shortest path matrix using Floyd-Warshall algorithm
    for k in range(N + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                if shortest_paths[i][k] + shortest_paths[k][j] < shortest_paths[i][j]:
                    shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]

    # Find the number of shortest paths containing each road
    num_shortest_paths = [0] * M
    for i in range(M):
        for j in range(M):
            if i != j and shortest_paths[roads[i][0]][roads[j][1]] == shortest_paths[roads[i][0]][roads[i][1]] + roads[j][2]:
                num_shortest_paths[i] += 1

    return num_shortest_paths

def get_output(num_shortest_paths):
    return [str(n) for n in num_shortest_paths]

if __name__ == '__main__':
    N, M, roads = get_input()
    num_shortest_paths = find_shortest_paths(N, M, roads)
    print('\n'.join(get_output(num_shortest_paths)))

