
def get_graph_from_input(v, edges):
    graph = [[] for _ in range(v)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def get_pigs_locations(pigs, graph):
    pigs_locations = {}
    for i, pig in enumerate(pigs):
        pigs_locations[i] = pig
    return pigs_locations

def get_distances(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances

def get_wolves_to_remove(graph, pigs_locations, pigs_number):
    distances = get_distances(graph, 0)
    wolves_to_remove = 0
    for i in range(pigs_number):
        pig = pigs_locations[i]
        if distances[pig] == float('inf'):
            wolves_to_remove += 1
    return wolves_to_remove

def main():
    v, p = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(v - 1)]
    pigs = list(map(int, input().split()))
    graph = get_graph_from_input(v, edges)
    pigs_locations = get_pigs_locations(pigs, graph)
    wolves_to_remove = get_wolves_to_remove(graph, pigs_locations, p)
    print(wolves_to_remove)

if __name__ == '__main__':
    main()

