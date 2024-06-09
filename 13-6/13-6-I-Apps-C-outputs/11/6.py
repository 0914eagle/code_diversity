
def f1(N):
    # Calculate the number of nodes in the tree
    num_nodes = 2**N - 1
    
    # Initialize an empty list to store the tree
    tree = []
    
    # Add the root node
    tree.append(1)
    
    # Add the left and right subtrees recursively
    add_subtrees(tree, 1, num_nodes)
    
    # Return the tree in preorder traversal
    return tree

def add_subtrees(tree, idx, num_nodes):
    # Base case: if the current node is a leaf node, return
    if idx >= num_nodes:
        return
    
    # Add the left subtree
    tree.append(idx*2)
    add_subtrees(tree, idx*2, num_nodes)
    
    # Add the right subtree
    tree.append(idx*2 + 1)
    add_subtrees(tree, idx*2 + 1, num_nodes)

if __name__ == '__main__':
    N = int(input())
    print(*f1(N))

