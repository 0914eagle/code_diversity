
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
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
                
                # Check if the output is correct
                pre_print = "".join(pre_output[:pre_calls])
                in_print = "".join(in_output[pre_calls:pre_calls+in_calls])
                post_print = "".join(post_output[pre_calls+in_calls:])
                if pre_print != in_print or pre_print != post_print:
                    continue
                
                # Add the reconstruction to the list
                reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

