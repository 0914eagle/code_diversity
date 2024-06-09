
def get_reconstruction(pre_output, in_output, post_output):
    # Initialize the possible reconstructions
    reconstructions = []
    
    # Loop through all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls is correct
                if pre_calls + in_calls + post_calls != 6:
                    continue
                
                # Check if the calls are in the correct order
                if pre_calls > in_calls or in_calls > post_calls:
                    continue
                
                # Check if the calls are in the correct routines
                if pre_calls != pre_output.count("Pre") or in_calls != in_output.count("In") or post_calls != post_output.count("Post"):
                    continue
                
                # Check if the calls are in the correct order in the routines
                if pre_output.index("Pre") > in_output.index("In") or in_output.index("In") > post_output.index("Post"):
                    continue
                
                # If all checks pass, add the reconstruction to the list
                reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

def get_first_tree(pre_output, in_output, post_output):
    # Initialize the first tree with the preorder output
    tree = pre_output
    
    # Loop through the inorder and postorder outputs
    for output in [in_output, post_output]:
        # Find the first occurrence of "In" or "Post" in the output
        index = output.index("In") if "In" in output else output.index("Post")
        
        # Add the corresponding letter to the tree
        tree += output[index]
    
    # Return the first tree
    return tree

if __name__ == '__main__':
    # Read the input from stdin
    pre_output = input()
    in_output = input()
    post_output = input()
    
    # Get the reconstruction
    reconstruction = get_reconstruction(pre_output, in_output, post_output)
    
    # Print the reconstruction
    print(reconstruction)
    
    # Get the first tree
    tree = get_first_tree(pre_output, in_output, post_output)
    
    # Print the first tree
    print(tree)

