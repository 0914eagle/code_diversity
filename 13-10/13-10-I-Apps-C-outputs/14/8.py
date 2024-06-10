
def read_graph():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return n, graph

def is_independent_set(graph, subset):
    for node in subset:
        for neighbor in graph[node]:
            if neighbor in subset:
                return False
    return True

def find_maximum_independent_set(graph):
    maximum_independent_set = []
    for node in graph:
        subset = [node]
        if is_independent_set(graph, subset):
            maximum_independent_set = subset
            break
    for node in graph:
        for neighbor in graph[node]:
            subset = [node, neighbor]
            if is_independent_set(graph, subset):
                maximum_independent_set = subset
                break
    return len(maximum_independent_set)

if __name__ == '__main__':
    n, graph = read_graph()
    print(find_maximum_independent_set(graph))

