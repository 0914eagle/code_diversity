
def is_acyclic(graph):
    # Check if the graph has a cycle
    visited = set()
    to_visit = [0]
    while to_visit:
        vertex = to_visit.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        to_visit += graph[vertex]
    return len(visited) == len(graph)

def remove_edge(graph):
    # Find an edge that can be removed to make the graph acyclic
    for vertex in range(len(graph)):
        for neighbor in graph[vertex]:
            if neighbor in graph[vertex]:
                graph[vertex].remove(neighbor)
                graph[neighbor].remove(vertex)
                return graph
    return graph

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
    if is_acyclic(graph):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

