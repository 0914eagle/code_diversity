
def is_spanning_tree_possible(n, m, k, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[1] - 1].append(edge[2] - 1)
        graph[edge[2] - 1].append(edge[1] - 1)

    # Initialize a count of blue edges to 0
    blue_edges = 0

    # Initialize a queue to perform BFS
    queue = [0]

    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)

        # If the node is not visited, mark it as visited and add it to the queue
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

            # If the node is blue, increment the blue edge count
            if edges[node][0] == "B":
                blue_edges += 1

    # Return True if the blue edge count is equal to k, False otherwise
    return blue_edges == k

# Main function
n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(str, input().split())))
print(is_spanning_tree_possible(n, m, k, edges))

