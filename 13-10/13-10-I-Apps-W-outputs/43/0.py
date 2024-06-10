
def get_vertices_to_delete(n, tree):
    
    # Initialize a list to store the vertices to delete
    vertices_to_delete = []
    
    # Loop through each vertex in the tree
    for i in range(1, n + 1):
        # If the vertex does not respect its parent and none of its children respect it, add it to the list of vertices to delete
        if tree[i][1] == 1 and all(tree[j][1] == 0 for j in tree[i][0]):
            vertices_to_delete.append(i)
    
    # If there are no vertices to delete, return -1
    if not vertices_to_delete:
        return -1
    
    # Return the list of vertices to delete
    return vertices_to_delete

def delete_vertices(n, tree, vertices_to_delete):
    
    # Loop through each vertex to delete
    for i in vertices_to_delete:
        # If the vertex has children, connect them with the parent of the vertex
        if tree[i][0]:
            for j in tree[i][0]:
                tree[tree[i][2]].append(j)
        
        # Remove the vertex and its children from the tree
        tree.pop(i)
        for j in tree[i][0]:
            tree.pop(j)
    
    # Return the resulting tree
    return tree

def main():
    # Read the number of vertices in the tree
    n = int(input())
    
    # Read the tree data
    tree = {}
    for i in range(1, n + 1):
        tree[i] = [int(x) for x in input().split()]
    
    # Get the indices of the vertices to delete
    vertices_to_delete = get_vertices_to_delete(n, tree)
    
    # Delete the vertices and print the resulting tree
    if vertices_to_delete != -1:
        print(*delete_vertices(n, tree, vertices_to_delete), sep='\n')
    else:
        print(-1)

if __name__ == '__main__':
    main()

