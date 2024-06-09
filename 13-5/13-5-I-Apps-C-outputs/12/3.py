
def f1(N, K):
    # Initialize a graph with N vertices
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the input data
    for i in range(N):
        for j in range(i+1, N):
            if i != j:
                graph[i].append(j)

    # Find the largest clique in the graph
    max_clique = find_largest_clique(graph, K)

    # Return the size of the largest clique
    return len(max_clique)

def f2(graph, K):
    # Initialize a list to store the maximum clique
    max_clique = []

    # Iterate over all possible subsets of the graph
    for subset in powerset(graph):
        # Check if the subset is a clique
        if is_clique(subset, K):
            # If it is a clique, add it to the list of maximum cliques
            max_clique.append(subset)

    # Return the largest clique
    return max(max_clique, key=len)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def is_clique(subset, K):
    # Check if the subset is a clique
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            if not (i, j) in K:
                return False
    return True

def find_largest_clique(graph, K):
    # Initialize a list to store the maximum clique
    max_clique = []

    # Iterate over all possible subsets of the graph
    for subset in powerset(graph):
        # Check if the subset is a clique
        if is_clique(subset, K):
            # If it is a clique, add it to the list of maximum cliques
            max_clique.append(subset)

    # Return the largest clique
    return max(max_clique, key=len)

if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(N):
        D = int(input())
        for _ in range(D):
            j = int(input())
            graph[i].append(j)
    print(f1(N, K))

