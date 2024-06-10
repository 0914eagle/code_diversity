
def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def remove_corridors(n, m, corridors):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v in corridors:
        graph[u].append(v)
        graph[v].append(u)

    # Remove edges to form a tree
    removed_edges = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and graph[j] and graph[i][0] == graph[j][0]:
                graph[i].remove(graph[i][0])
                graph[j].remove(graph[j][0])
                removed_edges += 1
                break

    # Return the removed edges
    return removed_edges

def main():
    n, m, corridors = get_input()
    print(remove_corridors(n, m, corridors))

if __name__ == '__main__':
    main()

