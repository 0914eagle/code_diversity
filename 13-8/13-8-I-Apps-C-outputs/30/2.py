
def is_bfs_order(n, edges, sequence):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a queue to perform BFS
    queue = [1]

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Perform BFS starting from node 1
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    # Check if all nodes are visited
    if len(visited) == n:
        return True

    # Check if the sequence is a valid BFS ordering
    for i, node in enumerate(sequence):
        if node not in visited:
            return False
        if i != sequence.index(node):
            return False

    return True

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edge = list(map(int, input().split()))
        edges.append(edge)
    sequence = list(map(int, input().split()))
    print("Yes") if is_bfs_order(n, edges, sequence) else print("No")

if __name__ == '__main__':
    main()

