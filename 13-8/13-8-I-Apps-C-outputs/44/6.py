
def get_cycle_length(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return len(visited)

def get_cycle_removal_plan(graph):
    removal_plan = []
    for node in graph:
        if get_cycle_length(graph, node) > 1:
            removal_plan.append(node)
    return removal_plan

def main():
    n, m = map(int, input().split())
    graph = {i: set() for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    removal_plan = get_cycle_removal_plan(graph)
    print(len(removal_plan))
    for node in removal_plan:
        print(node)

if __name__ == '__main__':
    main()

