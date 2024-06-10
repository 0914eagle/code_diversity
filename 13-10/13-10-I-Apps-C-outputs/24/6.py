
def get_graph(num_vertices, edges):
    graph = {}
    for edge in edges:
        u, v = edge[0], edge[1]
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
    return graph

def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def get_pigs_escaped(graph, pigs):
    visited = set()
    for pig in pigs:
        if pig not in visited:
            dfs(graph, pig, visited)
    return len(visited)

def get_min_wolves_to_remove(num_vertices, num_pigs, edges, initial_pigs):
    graph = get_graph(num_vertices, edges)
    initial_pigs.sort()
    min_wolves = 0
    for i in range(num_pigs):
        pigs_escaped = get_pigs_escaped(graph, initial_pigs[i+1:])
        if pigs_escaped < num_pigs - i:
            min_wolves += 1
    return min_wolves

def main():
    num_vertices, num_pigs = map(int, input().split())
    edges = []
    for _ in range(num_vertices-1):
        edges.append(list(map(int, input().split())))
    initial_pigs = list(map(int, input().split()))
    print(get_min_wolves_to_remove(num_vertices, num_pigs, edges, initial_pigs))

if __name__ == '__main__':
    main()

