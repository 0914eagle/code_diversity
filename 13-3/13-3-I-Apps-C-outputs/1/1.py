
def kahn_algorithm(graph):
    
    sorted_nodes = []
    while graph:
        sources = [node for node in graph if not graph[node]]
        if not sources:
            break
        source = sources[0]
        graph.pop(source)
        for neighbor in graph:
            graph[neighbor].discard(source)
        sorted_nodes.append(source)
    return sorted_nodes

def largest_s_size(graph):
    
    sources = [node for node in graph if not graph[node]]
    return len(sources)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        x, y = map(int, input().split())
        if x not in graph:
            graph[x] = set()
        graph[x].add(y)
    print(largest_s_size(graph))

