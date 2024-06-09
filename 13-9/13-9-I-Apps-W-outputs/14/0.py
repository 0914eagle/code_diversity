
def get_brain_latency(nervous_system):
    n, m = nervous_system
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in zip(*(iter(m),) * 2):
        graph[i].add(j)
        graph[j].add(i)
    visited = set()
    queue = [1]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue += graph[node] - visited
    return len(visited) - 1

