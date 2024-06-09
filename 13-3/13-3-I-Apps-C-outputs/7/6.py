
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls == 6:
                    # Initialize a list to store the calls for each routine
                    calls = []
                    
                    # Add the calls for the prePrint routine
                    for i in range(pre_calls):
                        calls.append("Pre")
                    
                    # Add the calls for the inPrint routine
                    for i in range(in_calls):
                        calls.append("In")
                    
                    # Add the calls for the postPrint routine
                    for i in range(post_calls):
                        calls.append("Post")
                    
                    # Check if the calls match the observed output
                    if "".join(calls) == pre_output and "".join(calls) == in_output and "".join(calls) == post_output:
                        # Initialize a list to store the trees
                        trees = []
                        
                        # Add the preorder print of the tree
                        trees.append(pre_output)
                        
                        # Add the inorder print of the tree
                        trees.append(in_output)
                        
                        # Add the postorder print of the tree
                        trees.append(post_output)
                        
                        # Add the reconstruction to the list of reconstructions
                        reconstructions.append((calls, trees))
    
    # Return the list of reconstructions
    return reconstructions

