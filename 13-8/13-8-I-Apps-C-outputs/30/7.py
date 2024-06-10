
def is_bfs_traversal(graph, sequence):
    # Initialize a queue to do BFS traversal
    queue = [1]
    visited = [False] * len(graph)
    visited[0] = True

    # Iterate through the sequence
    for node in sequence:
        # If the current node is not in the graph, return False
        if node not in graph:
            return False

        # If the current node is not visited, mark it as visited and add its neighbors to the queue
        if not visited[node - 1]:
            visited[node - 1] = True
            queue.extend(graph[node])

    # If all nodes are visited and the queue is empty, return True
    return all(visited) and not queue

def main():
    n = int(input())
    graph = {}
    for _ in range(n - 1):
        x, y = map(int, input().split())
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y)
        graph[y].append(x)
    sequence = list(map(int, input().split()))
    print("Yes") if is_bfs_traversal(graph, sequence) else print("No")

if __name__ == '__main__':
    main()

