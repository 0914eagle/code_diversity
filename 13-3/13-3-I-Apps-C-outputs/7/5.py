
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls == 6:
                    # Check if the calls to each routine are in the correct order
                    if (pre_calls == 0 or pre_calls == 2) and (in_calls == 1 or in_calls == 3) and (post_calls == 4 or post_calls == 5):
                        # Check if the outputs match the given outputs
                        if (pre_output == "".join(reversed(pre_output)) and in_output == "".join(reversed(in_output)) and post_output == "".join(reversed(post_output))):
                            # Add the reconstruction to the list
                            reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

