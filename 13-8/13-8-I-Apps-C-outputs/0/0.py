
def is_reachable(n, edges):
    # Initialize a dictionary to store the values of the edges
    values = {(i+1, j+1): 0 for i in range(n-1) for j in range(i+1, n)}
    values[(1, n)] = 0
    
    # Initialize a queue to store the nodes to be processed
    queue = [(1, n)]
    
    while queue:
        # Dequeue a node
        node = queue.pop(0)
        
        # If the node is a leaf, add the value of the edge to the value of the parent node
        if node[0] == node[1]:
            values[node] += 1
        
        # If the node has a parent, enqueue the parent node
        if node[0] != 1:
            queue.append((node[0], node[1]))
    
    # If all the edges have a non-zero value, return True
    return all(values[edge] != 0 for edge in edges)

def main():
    n = int(input())
    edges = []
    
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    print("YES" if is_reachable(n, edges) else "NO")

if __name__ == '__main__':
    main()

