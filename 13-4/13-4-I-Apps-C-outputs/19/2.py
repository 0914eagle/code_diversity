
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize an empty list to store the reconstructions
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
                
                # Check if the outputs match the given outputs
                if not check_outputs(pre_output, in_output, post_output, pre_calls, in_calls, post_calls):
                    continue
                
                # If all conditions are met, add the reconstruction to the list
                reconstructions.append([pre_calls, in_calls, post_calls])
    
    # Return the list of reconstructions
    return reconstructions

def check_outputs(pre_output, in_output, post_output, pre_calls, in_calls, post_calls):
    # Initialize variables to store the current outputs
    current_pre_output = ""
    current_in_output = ""
    current_post_output = ""
    
    # Iterate over the calls to each routine
    for i in range(6):
        # Check if the current call is to Pre, In, or Post
        if i < pre_calls:
            current_pre_output += pre_output[i]
        elif i < pre_calls + in_calls:
            current_in_output += in_output[i - pre_calls]
        else:
            current_post_output += post_output[i - pre_calls - in_calls]
    
    # Check if the current outputs match the given outputs
    return current_pre_output == pre_output and current_in_output == in_output and current_post_output == post_output

pre_output = "HFBIGEDCJA"
in_output = "BIGEDCJFAH"
post_output = "BIGEDCJFAH"
reconstructions = get_reconstructions(pre_output, in_output, post_output)
print(reconstructions)

