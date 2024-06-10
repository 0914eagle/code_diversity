
def is_reachable(graph, values):
    # Initialize a queue to do breadth-first search
    queue = [(0, 0)]
    
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    # Loop until the queue is empty
    while queue:
        # Get the current node and its value from the queue
        node, value = queue.pop(0)
        
        # If the current node is a leaf and its value is not equal to the target value, return False
        if node not in graph and value != values[node]:
            return False
        
        # If the current node is not a leaf and its value is not equal to the target value, return False
        if node in graph and value != values[node]:
            return False
        
        # If the current node is a leaf and its value is equal to the target value, add its neighbors to the queue
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, values[node]))
                    visited.add(neighbor)
    
    # If the queue is empty and all nodes have been visited, return True
    return True

def main():
    # Read the number of nodes and edges from stdin
    n, m = map(int, input().split())
    
    # Read the edges from stdin
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    
    # Read the values from stdin
    values = {}
    for _ in range(n):
        u, v = map(int, input().split())
        values[u] = v
    
    # Check if the values are reachable from the root
    if is_reachable(graph, values):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

