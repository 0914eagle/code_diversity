
def bfs_traversal(graph, start):
    # Initialize a queue for BFS
    queue = [start]

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)

        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    # If all nodes in the graph have been visited, return True, otherwise return False
    return len(visited) == len(graph)

def check_sequence(graph, sequence):
    # Initialize the start node as 1
    start = 1

    # Loop through the sequence
    for node in sequence:
        # If the current node is not in the graph, return False
        if node not in graph:
            return False

        # If the current node is not a neighbor of the previous node, return False
        if node not in graph[start]:
            return False

        # Update the start node to the current node
        start = node

    # If all nodes in the sequence are valid, return True
    return True

def main():
    # Read the input data
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

    # Check if the sequence corresponds to a valid BFS traversal of the graph
    result = check_sequence(graph, sequence)

    # Print the result
    print("Yes") if result else print("No")

if __name__ == '__main__':
    main()

