
def is_reachable(graph, values):
    # Initialize a queue to do breadth-first search
    queue = [(0, 0)]
    
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    while queue:
        # Dequeue a node from the queue
        node, value = queue.pop(0)
        
        # If the node is a leaf and its value is not equal to the desired value, return False
        if node not in graph and value != values[node]:
            return False
        
        # If the node is not a leaf and its value is not equal to the sum of its children's values, return False
        if node in graph and value != sum(values[child] for child in graph[node]):
            return False
        
        # If the node has not been visited yet, mark it as visited and enqueue its neighbors
        if node not in visited:
            visited.add(node)
            queue.extend((neighbor, values[neighbor]) for neighbor in graph[node])
    
    # If all nodes have been visited and the values are correct, return True
    return True

def solve(n, edges):
    # Initialize a graph with the given edges
    graph = {u: set() for u in range(1, n + 1)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Initialize a dictionary to keep track of the values on the edges
    values = {u: 0 for u in range(1, n + 1)}
    
    # Return whether it is possible to reach the desired configuration using the given operations
    return is_reachable(graph, values)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES") if solve(n, edges) else print("NO")

