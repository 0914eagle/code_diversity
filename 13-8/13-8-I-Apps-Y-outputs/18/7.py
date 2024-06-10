
def get_diameter(n, m, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Find the diameter of the graph
    diameter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and j in graph[i]:
                diameter = max(diameter, len(graph[i]) + len(graph[j]))

    return diameter

def add_edges(n, m, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Find the diameter of the graph
    diameter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and j in graph[i]:
                diameter = max(diameter, len(graph[i]) + len(graph[j]))

    # If the graph is already a tree, return
    if diameter == 0:
        return []

    # Otherwise, add edges to form a tree
    added_edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and j in graph[i]:
                added_edges.append((i, j))
                graph[i].remove(j)
                graph[j].remove(i)
                break

    return added_edges

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    diameter = get_diameter(n, m, edges)
    added_edges = add_edges(n, m, edges)
    print(diameter)
    for edge in added_edges:
        print(*edge)

if __name__ == '__main__':
    main()

