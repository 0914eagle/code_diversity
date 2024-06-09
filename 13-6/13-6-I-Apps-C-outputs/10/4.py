
def get_maximum_protected_rooms(N, M, doors):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the doors
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)

    # Find the node with the most neighbors
    max_neighbors = 0
    node_with_max_neighbors = 0
    for i in range(N):
        neighbors = len(graph[i])
        if neighbors > max_neighbors:
            max_neighbors = neighbors
            node_with_max_neighbors = i

    # Return the maximum number of protected rooms
    return max_neighbors

def main():
    N, M = map(int, input().split())
    doors = []
    for _ in range(M):
        u, v = map(int, input().split())
        doors.append((u, v))
    print(get_maximum_protected_rooms(N, M, doors))

if __name__ == '__main__':
    main()

