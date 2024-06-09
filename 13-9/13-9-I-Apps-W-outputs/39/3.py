
def get_max_water_amount(n, p, k, pipes, improvements):
    # Initialize the graph with the given pipes
    graph = {i: set() for i in range(1, n + 1)}
    for a, b, c in pipes:
        graph[a].add((b, c))
        graph[b].add((a, c))

    # Initialize the max water amount with the initial configuration
    max_water_amount = 0
    for a, b, c in improvements:
        # If the pipe does not exist, create it with the given capacity
        if (a, b) not in graph:
            graph[a].add((b, c))
            graph[b].add((a, c))
        # If the pipe exists, increase its capacity
        else:
            graph[a].remove((b, graph[a][(b, c)][1]))
            graph[a].add((b, c + graph[a][(b, c)][1]))
            graph[b].remove((a, graph[b][(a, c)][1]))
            graph[b].add((a, c + graph[b][(a, c)][1]))

        # Calculate the max water amount after the improvement
        max_water_amount = max(max_water_amount, get_max_flow(graph, 1, 3))

    return [max_water_amount] + [get_max_flow(graph, 1, 3) for _ in range(k)]

def get_max_flow(graph, start, end):
    # Initialize the max flow with the initial capacity
    max_flow = graph[start][(end, 0)][1]

    # Breadth-first search to find the max flow
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, flow = queue.pop(0)
        if node == end:
            max_flow = max(max_flow, flow)
            continue
        if node in visited:
            continue
        visited.add(node)
        for neighbor, capacity in graph[node]:
            if flow + capacity > max_flow:
                queue.append((neighbor, flow + capacity))

    return max_flow

n = int(input())
p = int(input())
k = int(input())
pipes = []
for _ in range(p):
    a, b, c = map(int, input().split())
    pipes.append((a, b, c))
improvements = []
for _ in range(k):
    a, b, c = map(int, input().split())
    improvements.append((a, b, c))
result = get_max_water_amount(n, p, k, pipes, improvements)
print(*result)

