
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls == 6:
                    # Check if the output of the three routines matches the given output
                    if (pre_output == "".join(sorted(pre_output)) and
                        in_output == "".join(sorted(in_output)) and
                        post_output == "".join(sorted(post_output))):
                        # If the output matches, add the reconstruction to the list
                        reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

