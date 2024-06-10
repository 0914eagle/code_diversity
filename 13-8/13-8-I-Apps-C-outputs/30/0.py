
def is_bfs_traversal(graph, sequence):
    
    # Initialize a queue to store the nodes to visit
    queue = [1]
    # Initialize a set to keep track of the visited nodes
    visited = set()
    # Iterate through the sequence
    for node in sequence:
        # If the node is not in the graph, return False
        if node not in graph:
            return False
        # If the node is already visited, return False
        if node in visited:
            return False
        # If the node is not at the front of the queue, return False
        if node != queue[0]:
            return False
        # Add the node to the visited set
        visited.add(node)
        # Extract the node from the queue
        queue.pop(0)
        # Add the node's neighbors to the back of the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    # If all nodes are visited and the queue is empty, return True
    return len(visited) == len(graph) and not queue

def main():
    # Read the input
    num_nodes = int(input())
    graph = {}
    for _ in range(num_nodes - 1):
        node1, node2 = map(int, input().split())
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)
        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)
    sequence = list(map(int, input().split()))
    # Determine whether the sequence is a valid BFS traversal
    if is_bfs_traversal(graph, sequence):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

