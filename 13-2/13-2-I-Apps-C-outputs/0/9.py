
def is_spanning_tree_possible(n, m, k, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for c, f, t in edges:
        graph[f - 1].append((c, t - 1))
        graph[t - 1].append((c, f - 1))

    # Initialize a variable to keep track of the number of blue edges
    num_blue_edges = 0

    # Initialize a queue to perform BFS
    queue = [0]

    # Loop through the graph until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)

        # Check if the node has any unvisited neighbors
        for neighbor, color in graph[node]:
            if color == "B":
                num_blue_edges += 1
            if neighbor not in queue:
                queue.append(neighbor)

    # Check if the number of blue edges is equal to k
    return num_blue_edges == k

n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    c, f, t = input().split()
    edges.append((c, int(f), int(t)))
print(is_spanning_tree_possible(n, m, k, edges))

