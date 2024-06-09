
def get_maximum_clique(A):
    # Initialize a graph with the given set of numbers as vertices
    graph = {a: set() for a in A}

    # Add edges between vertices based on divisibility relationship
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] % A[j] == 0 or A[j] % A[i] == 0:
                graph[A[i]].add(A[j])
                graph[A[j]].add(A[i])

    # Find the maximum clique in the graph
    clique = []
    for a in A:
        clique.append(get_clique(a, graph))

    return max(clique)

def get_clique(a, graph):
    visited = set()
    queue = [a]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex] - visited

    return len(visited)

