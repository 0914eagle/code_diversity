
def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def remove_corridors(n, m, corridors):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v in corridors:
        graph[u].append(v)

    # Find all cycles in the graph
    cycles = []
    for u in range(1, n + 1):
        for v in graph[u]:
            if v in graph[u]:
                cycles.append((u, v))

    # Remove at most half of the corridors to break the cycles
    removed_corridors = set()
    for u, v in cycles:
        if len(removed_corridors) < m // 2:
            removed_corridors.add((u, v))

    return removed_corridors

def get_output(removed_corridors):
    return len(removed_corridors), *removed_corridors

if __name__ == '__main__':
    n, m, corridors = get_input()
    removed_corridors = remove_corridors(n, m, corridors)
    print(*get_output(removed_corridors))

