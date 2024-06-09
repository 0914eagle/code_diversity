
def get_reconstruction(pre_output, in_output, post_output):
    # Initialize the possible calls for each routine
    pre_calls = ["Pre", "Post"]
    in_calls = ["In"]
    post_calls = ["Pre", "Post"]
    
    # Initialize the possible trees
    trees = []
    
    # Loop through all possible combinations of calls
    for pre_call1 in pre_calls:
        for pre_call2 in pre_calls:
            for in_call in in_calls:
                for post_call1 in post_calls:
                    for post_call2 in post_calls:
                        # Check if the current combination of calls generates the observed outputs
                        if (pre_call1 + pre_call2 + in_call + post_call1 + post_call2) == pre_output and (pre_call1 + in_call + post_call1 + post_call2) == in_output and (pre_call1 + pre_call2 + in_call + post_call1 + post_call2) == post_output:
                            # If the current combination of calls generates the observed outputs, add the corresponding tree to the list of possible trees
                            trees.append((pre_call1 + pre_call2 + in_call + post_call1 + post_call2, pre_call1 + in_call + post_call1 + post_call2, pre_call1 + pre_call2 + in_call + post_call1 + post_call2))
    
    # Return the list of possible trees
    return trees

