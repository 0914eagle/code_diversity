
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls is correct
                if pre_calls + in_calls + post_calls != 6:
                    continue
                
                # Check if the calls are in the correct order
                if pre_calls > in_calls or in_calls > post_calls:
                    continue
                
                # Check if the calls are valid
                if pre_calls * "Pre" + in_calls * "In" + post_calls * "Post" not in pre_output + in_output + post_output:
                    continue
                
                # Find the first tree with the observed output
                tree = find_tree(pre_output, in_output, post_output, pre_calls, in_calls, post_calls)
                
                # Add the reconstruction to the list
                reconstructions.append([pre_calls, in_calls, post_calls, tree])
    
    # Sort the reconstructions lexicographically
    reconstructions.sort(key=lambda x: (x[0], x[1], x[2]))
    
    # Return the list of reconstructions
    return reconstructions

def find_tree(pre_output, in_output, post_output, pre_calls, in_calls, post_calls):
    # Initialize a list to store the possible trees
    trees = []
    
    # Iterate over all possible trees
    for tree in itertools.permutations("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        # Check if the tree has the observed output
        if get_output(tree, pre_calls, in_calls, post_calls) == pre_output + in_output + post_output:
            # Add the tree to the list
            trees.append(tree)
    
    # Return the first tree with the observed output
    return trees[0]

def get_output(tree, pre_calls, in_calls, post_calls):
    # Initialize the output strings
    pre_output = ""
    in_output = ""
    post_output = ""
    
    # Iterate over the tree
    for i in range(len(tree)):
        # Get the current node
        node = tree[i]
        
        # Add the node to the output strings
        pre_output += node
        in_output += node
        post_output += node
        
        # Add the recursive calls to the output strings
        if i < len(tree) - 1:
            pre_output += " " + tree[i + 1]
            in_output += " " + tree[i + 1]
            post_output += " " + tree[i + 1]
    
    # Return the output strings
    return pre_output, in_output, post_output

