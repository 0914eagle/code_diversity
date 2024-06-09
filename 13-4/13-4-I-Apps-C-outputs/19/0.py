
def find_reconstructions(pre_output, in_output, post_output):
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
                
                # Check if the outputs match
                if pre_output != "".join(sorted(pre_output)) or in_output != "".join(sorted(in_output)) or post_output != "".join(sorted(post_output)):
                    continue
                
                # If all checks pass, add the reconstruction to the list
                reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

