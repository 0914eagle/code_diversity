
def is_valid_bfs(n, edges, sequence):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Initialize a queue to perform BFS
    queue = [0]

    # Mark the first node as visited
    visited = [False] * n
    visited[0] = True

    # Loop through the sequence
    for i in range(n):
        # If the current node is not in the graph, return False
        if sequence[i] not in graph:
            return False

        # If the current node is not visited, mark it as visited and add its neighbors to the queue
        if not visited[sequence[i] - 1]:
            visited[sequence[i] - 1] = True
            queue += graph[sequence[i] - 1]

        # If the queue is empty and not all nodes are visited, return False
        if not queue and not all(visited):
            return False

        # If the queue is not empty, dequeue a node and mark it as visited
        if queue:
            node = queue.pop(0)
            visited[node] = True

    # If all nodes are visited, return True
    return all(visited)

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    sequence = list(map(int, input().split()))
    print("Yes") if is_valid_bfs(n, edges, sequence) else print("No")

if __name__ == '__main__':
    main()

