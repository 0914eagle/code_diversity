
def kahn_algorithm(graph):
    
    sorted_list = []
    while graph:
        sources = [node for node in graph if not graph[node]]
        if not sources:
            break
        source = sources[0]
        graph.pop(source)
        for neighbor in graph[source]:
            graph[neighbor].remove(source)
            if not graph[neighbor]:
                sources.append(neighbor)
        sorted_list.append(source)
    return sorted_list

def largest_s_size(graph):
    
    largest_s_size = 0
    for node in graph:
        incoming_edges = graph[node]
        if not incoming_edges:
            largest_s_size = max(largest_s_size, 1)
        else:
            largest_s_size = max(largest_s_size, len(incoming_edges) + 1)
    return largest_s_size

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        x, y = map(int, input().split())
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y)
    print(largest_s_size(graph))

