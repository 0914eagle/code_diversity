
def solve(n, m):
    # Initialize the graph with two vertices s and t
    graph = {s: [], t: []}

    # Perform the given number of changes
    for i in range(n):
        # Add a new vertex w
        w = chr(ord('a') + i)
        graph[w] = []

        # Choose an existing edge (u, v)
        u, v = random.sample(graph.items(), 2)

        # Add the new edges (u, w) and (v, w)
        graph[u].append(w)
        graph[v].append(w)
        graph[w].append(u)
        graph[w].append(v)

    # Find the minimum s-t cut
    min_cut = find_min_cut(graph, m)

    # Count the number of non-similar worlds
    num_worlds = count_non_similar_worlds(graph, min_cut)

    return num_worlds

def find_min_cut(graph, m):
    # Find the minimum cut by performing a BFS from s and t and counting the number of edges
    visited = set()
    queue = [graph['s']]
    while queue:
        vertex = queue.pop(0)
        if vertex == graph['t']:
            return len(visited)
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]

def count_non_similar_worlds(graph, min_cut):
    # Count the number of non-similar worlds by performing a DFS and checking for isomorphism
    num_worlds = 0
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            num_worlds += count_non_similar_subworlds(graph, vertex, min_cut, visited)

    return num_worlds

def count_non_similar_subworlds(graph, vertex, min_cut, visited):
    # Count the number of non-similar subworlds by performing a DFS and checking for isomorphism
    num_worlds = 0
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            num_worlds += count_non_similar_subworlds(graph, neighbor, min_cut, visited)

    return num_worlds

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve(n, m))

