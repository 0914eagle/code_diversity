
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize an empty list to store the reconstructions
    reconstructions = []
    
    # Loop through all possible combinations of Pre, In, and Post calls
    for pre_calls in range(2):
        for in_calls in range(2):
            for post_calls in range(2):
                # Check if the number of calls to each routine is correct
                if pre_calls + in_calls + post_calls == 6:
                    # Check if the output of the routines matches the given output
                    if (pre_output == "".join(pre_calls * "H") + "".join(in_calls * "B") + "".join(post_calls * "I")) and (in_output == "".join(pre_calls * "F") + "".join(in_calls * "A") + "".join(post_calls * "G")) and (post_output == "".join(pre_calls * "J") + "".join(in_calls * "C") + "".join(post_calls * "E")):
                        # Add the reconstruction to the list
                        reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

