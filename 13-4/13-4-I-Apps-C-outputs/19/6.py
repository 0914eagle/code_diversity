
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls != 6:
                    continue
                
                # Check if the calls to each routine are in the correct order
                if pre_calls > in_calls or in_calls > post_calls:
                    continue
                
                # Check if the calls to each routine are unique
                if pre_calls != in_calls and pre_calls != post_calls and in_calls != post_calls:
                    continue
                
                # Check if the outputs match the given outputs
                pre_print = "".join(pre_output[i] for i in range(pre_calls))
                in_print = "".join(in_output[i] for i in range(in_calls))
                post_print = "".join(post_output[i] for i in range(post_calls))
                if pre_print != pre_output or in_print != in_output or post_print != post_output:
                    continue
                
                # If all checks pass, add the reconstruction to the list
                reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

