
def f1(N, K, D):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the disagreements in the Book of Great Achievements
    for i in range(N):
        for j in range(i+1, N):
            if i not in D[j] and j not in D[i]:
                graph[i].append(j)
                graph[j].append(i)

    # Find the largest independent set in the graph
    return max(independent_set(graph, K))

def f2(graph, K):
    # Initialize a list to store the independent sets
    independent_sets = []

    # Iterate over all possible independent sets
    for i in range(1, len(graph) + 1):
        for subset in combinations(graph, i):
            # Check if the subset is independent
            if is_independent_set(subset, K):
                independent_sets.append(subset)

    # Return the largest independent set
    return max(independent_sets, key=len)

def independent_set(graph, K):
    # Initialize a list to store the independent sets
    independent_sets = []

    # Iterate over all possible independent sets
    for i in range(1, len(graph) + 1):
        for subset in combinations(graph, i):
            # Check if the subset is independent
            if is_independent_set(subset, K):
                independent_sets.append(subset)

    # Return the largest independent set
    return max(independent_sets, key=len)

def is_independent_set(subset, K):
    # Initialize a set to store the nodes in the subset
    nodes = set(subset)

    # Iterate over all nodes in the subset
    for i in nodes:
        # Check if the node has at least K neighbors in the subset
        if len(nodes.intersection(graph[i])) < K:
            return False

    # If all nodes have at least K neighbors in the subset, return True
    return True

if __name__ == '__main__':
    N, K = map(int, input().split())
    D = [set(map(int, input().split())) for _ in range(N)]
    print(f1(N, K, D))

