
def get_max_reachable_vertices(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])
    
    # Initialize two plans with the same undirected edges but different directions
    plan1 = ["-"] * m
    plan2 = ["+"] * m
    
    # Initialize two sets to keep track of reachable vertices
    reachable1 = set([s])
    reachable2 = set([s])
    
    # Iterate through the undirected edges and orient them in both plans
    for i in range(m):
        edge = edges[i]
        if edge[2] == 1:
            continue
        for j in range(2):
            if j == 0:
                reachable1 = get_reachable_vertices(graph, reachable1, edge[0], edge[1])
                plan1[i] = "+"
            else:
                reachable2 = get_reachable_vertices(graph, reachable2, edge[0], edge[1])
                plan2[i] = "-"
    
    return (len(reachable1), "".join(plan1)), (len(reachable2), "".join(plan2))

def get_reachable_vertices(graph, reachable, u, v):
    if v in reachable:
        return reachable
    reachable.add(v)
    for neighbor in graph[v - 1]:
        if neighbor != u and neighbor not in reachable:
            reachable = get_reachable_vertices(graph, reachable, v, neighbor)
    return reachable

def main():
    n, m, s = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(get_max_reachable_vertices(n, m, s, edges))

if __name__ == '__main__':
    main()

