
def f1(N, K):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the input
    for i in range(N):
        for j in range(i+1, N):
            if i != j:
                graph[i].append(j)

    # Find the largest clique in the graph
    clique = []
    for i in range(N):
        if i not in clique:
            clique = find_clique(graph, i, K)

    return len(clique)

def find_clique(graph, node, K):
    # Base case: if the node has no neighbors, return the node
    if not graph[node]:
        return [node]

    # Recursive case: find the largest clique among the node's neighbors
    max_clique = []
    for neighbor in graph[node]:
        if neighbor not in max_clique:
            max_clique = find_clique(graph, neighbor, K)

    # Add the node to the largest clique
    max_clique.append(node)

    # If the largest clique has size K, return it
    if len(max_clique) == K:
        return max_clique

    # Otherwise, find the node with the largest number of neighbors in the clique
    node_with_most_neighbors = 0
    for node in max_clique:
        if len(graph[node]) > len(graph[node_with_most_neighbors]):
            node_with_most_neighbors = node

    # Remove the node with the largest number of neighbors from the clique
    max_clique.remove(node_with_most_neighbors)

    # Recursively find the largest clique among the remaining nodes
    return find_clique(graph, node_with_most_neighbors, K)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(f1(N, K))

