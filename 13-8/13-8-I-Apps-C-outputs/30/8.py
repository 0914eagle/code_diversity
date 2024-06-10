
def bfs_traversal(tree, start):
    
    # Initialize the queue and mark the start vertex as used
    queue = [start]
    used = set([start])
    
    # Loop until the queue is empty
    while queue:
        # Extract a vertex from the head of the queue
        vertex = queue.pop(0)
        
        # Print the vertex
        print(vertex)
        
        # Iterate through all neighbors of the vertex that are not marked yet
        for neighbor in tree[vertex]:
            if neighbor not in used:
                # Mark the neighbor as used and insert it into the queue
                used.add(neighbor)
                queue.append(neighbor)
    
    # Return the traversal sequence
    return used

def is_valid_bfs_traversal(tree, sequence):
    
    # Initialize the start vertex as 1
    start = 1
    
    # Perform the BFS traversal and get the traversal sequence
    traversal = bfs_traversal(tree, start)
    
    # Check if the traversal sequence is the same as the given sequence
    return traversal == set(sequence)

def main():
    # Read the input data
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
    sequence = list(map(int, input().split()))
    
    # Check if the sequence is a valid BFS traversal of the tree
    if is_valid_bfs_traversal(tree, sequence):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

