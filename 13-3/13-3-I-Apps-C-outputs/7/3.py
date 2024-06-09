
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls == 6:
                    # Create a list to store the calls for each routine
                    calls = []
                    
                    # Add the Pre calls to the list
                    for i in range(pre_calls):
                        calls.append("Pre")
                    
                    # Add the In calls to the list
                    for i in range(in_calls):
                        calls.append("In")
                    
                    # Add the Post calls to the list
                    for i in range(post_calls):
                        calls.append("Post")
                    
                    # Sort the calls in lexicographic order
                    calls.sort()
                    
                    # Create a list to store the first tree with the observed output
                    first_tree = []
                    
                    # Iterate over all possible trees
                    for tree in generate_trees(pre_output, in_output, post_output):
                        # Check if the current tree has the observed output
                        if tree_output(tree) == (pre_output, in_output, post_output):
                            # Add the tree to the list
                            first_tree.append(tree)
                            
                            # Break out of the loop
                            break
                    
                    # Check if a tree with the observed output was found
                    if first_tree:
                        # Add the reconstruction to the list of reconstructions
                        reconstructions.append((calls, first_tree[0]))
    
    # Return the list of reconstructions
    return reconstructions

def generate_trees(pre_output, in_output, post_output):
    # Yield the empty tree
    yield []
    
    # Iterate over the characters in the preorder output
    for char in pre_output:
        # Iterate over the remaining characters in the preorder output
        for remaining in generate_trees(pre_output[1:], in_output, post_output):
            # Yield the tree with the current character as the root and the remaining characters as the children
            yield [char] + remaining

def tree_output(tree):
    # Return the preorder, inorder, and postorder outputs of the tree
    return (preorder(tree), inorder(tree), postorder(tree))

def preorder(tree):
    # Check if the tree is empty
    if not tree:
        # Return an empty string
        return ""
    
    # Return the current character followed by the preorder outputs of the children
    return tree[0] + preorder(tree[1:])

def inorder(tree):
    # Check if the tree is empty
    if not tree:
        # Return an empty string
        return ""
    
    # Return the inorder outputs of the children followed by the current character
    return inorder(tree[1:]) + tree[0]

def postorder(tree):
    # Check if the tree is empty
    if not tree:
        # Return an empty string
        return ""
    
    # Return the postorder outputs of the children followed by the current character
    return postorder(tree[1:]) + tree[0]

