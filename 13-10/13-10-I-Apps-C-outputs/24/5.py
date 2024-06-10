
def get_minimum_wolves_to_remove(tree):
    # Initialize a dictionary to store the number of wolves on each vertex
    num_wolves = {}
    for vertex in tree:
        num_wolves[vertex] = 0
    
    # Iterate through the tree and count the number of wolves on each vertex
    for vertex in tree:
        for neighbor in tree[vertex]:
            if neighbor in num_wolves:
                num_wolves[neighbor] += 1
    
    # Initialize a queue to store the vertices to be processed
    queue = []
    
    # Add the vertices with no wolves to the queue
    for vertex in tree:
        if num_wolves[vertex] == 0:
            queue.append(vertex)
    
    # Initialize a variable to store the minimum number of wolves to remove
    min_wolves = 0
    
    # Iterate through the queue and remove wolves from the vertices with no wolves
    while queue:
        vertex = queue.pop(0)
        if num_wolves[vertex] > 0:
            min_wolves += num_wolves[vertex]
            for neighbor in tree[vertex]:
                if neighbor in num_wolves:
                    num_wolves[neighbor] -= 1
                    if num_wolves[neighbor] == 0:
                        queue.append(neighbor)
    
    return min_wolves

def main():
    # Read the input data
    num_vertices, num_pigs = map(int, input().split())
    tree = {}
    for _ in range(num_vertices - 1):
        u, v = map(int, input().split())
        if u in tree:
            tree[u].append(v)
        else:
            tree[u] = [v]
    
    pigs = list(map(int, input().split()))
    
    # Call the function to get the minimum number of wolves to remove
    min_wolves = get_minimum_wolves_to_remove(tree)
    
    # Print the output
    print(min_wolves)

if __name__ == '__main__':
    main()

