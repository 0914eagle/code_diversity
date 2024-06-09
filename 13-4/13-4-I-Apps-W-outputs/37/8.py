
def get_independent_sets(graph):
    independent_sets = []
    for i in range(1, len(graph) + 1):
        for subset in itertools.combinations(graph, i):
            if is_independent_set(subset, graph):
                independent_sets.append(subset)
    return independent_sets

def is_independent_set(subset, graph):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if (subset[i], subset[j]) in graph:
                return False
    return True

def get_edge_induced_subgraphs(graph):
    edge_induced_subgraphs = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if (graph[i], graph[j]) not in edge_induced_subgraphs:
                edge_induced_subgraphs.append((graph[i], graph[j]))
    return edge_induced_subgraphs

def get_sum_of_independent_sets(graph):
    sum_of_independent_sets = 0
    for edge_induced_subgraph in get_edge_induced_subgraphs(graph):
        sum_of_independent_sets += len(get_independent_sets(edge_induced_subgraph))
    return sum_of_independent_sets % 998244353

if __name__ == '__main__':
    n = int(input())
    graph = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        graph.append((u, v))
    print(get_sum_of_independent_sets(graph))

