
def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def remove_corridors(n, m, corridors):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n + 1)]
    for u, v in corridors:
        graph[u].append(v)
    
    # Remove edges from the graph to form a tree
    removed_edges = set()
    for u in range(1, n + 1):
        for v in graph[u]:
            if v not in removed_edges:
                removed_edges.add((u, v))
                removed_edges.add((v, u))
                break
    
    # Return the number of edges removed and the edges that need to be removed
    return len(removed_edges), removed_edges

def main():
    n, m, corridors = get_input()
    r, removed_edges = remove_corridors(n, m, corridors)
    print(r)
    for u, v in removed_edges:
        print(u, v)

if __name__ == '__main__':
    main()

