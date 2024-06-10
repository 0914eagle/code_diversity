
def is_valid_bfs_order(n, edges, sequence):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize the queue with vertex 1
    queue = [1]

    # Initialize the visited array with False values
    visited = [False] * (n + 1)

    # Mark vertex 1 as visited
    visited[1] = True

    # Loop through the sequence
    for i in range(len(sequence)):
        # If the current vertex is not in the graph, return False
        if sequence[i] not in graph:
            return False

        # If the current vertex is not visited, mark it as visited and add its neighbors to the queue
        if not visited[sequence[i]]:
            visited[sequence[i]] = True
            queue += graph[sequence[i]]

        # If the queue is empty and we have visited all the vertices, return True
        if not queue and all(visited):
            return True

    # If we reach this point, it means that not all vertices were visited, so return False
    return False

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    sequence = list(map(int, input().split()))
    print("Yes") if is_valid_bfs_order(n, edges, sequence) else print("No")

if __name__ == '__main__':
    main()

