
def find_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Loop through all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls != 6:
                    continue
                
                # Check if the output of each routine is correct
                pre_print = "".join(pre_output[:pre_calls])
                in_print = "".join(in_output[pre_calls:pre_calls+in_calls])
                post_print = "".join(post_output[pre_calls+in_calls:])
                if pre_print != in_print or pre_print != post_print:
                    continue
                
                # Check if the calls to each routine are correct
                pre_calls_str = "Pre" * pre_calls
                in_calls_str = "In" * in_calls
                post_calls_str = "Post" * post_calls
                if pre_calls_str + in_calls_str + post_calls_str not in ["Pre Pre In In Post Post", "Pre In Pre In Post Post", "In Pre Pre In Post Post", "In Pre In Pre Post Post"]:
                    continue
                
                # If all checks pass, add the reconstruction to the list
                reconstructions.append([pre_calls_str, in_calls_str, post_calls_str])
    
    # Return the list of reconstructions
    return reconstructions

