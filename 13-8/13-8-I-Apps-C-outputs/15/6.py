
def find_reconstruction(pre_output, in_output, post_output):
    # Find all possible combinations of Pre, In, and Post calls
    combinations = []
    for pre in range(2):
        for in_ in range(2):
            for post in range(2):
                combinations.append([pre, in_, post])
    
    # Filter out combinations that do not match the observed outputs
    filtered_combinations = []
    for combination in combinations:
        pre_calls = combination[0]
        in_calls = combination[1]
        post_calls = combination[2]
        if pre_calls * "Pre" + in_calls * "In" + post_calls * "Post" == pre_output:
            if in_calls * "Pre" + post_calls * "In" + pre_calls * "Post" == in_output:
                if post_calls * "Pre" + in_calls * "In" + pre_calls * "Post" == post_output:
                    filtered_combinations.append(combination)
    
    # Find the first tree that generates the observed outputs for each combination
    reconstructions = []
    for combination in filtered_combinations:
        pre_calls = combination[0]
        in_calls = combination[1]
        post_calls = combination[2]
        preorder_print = ""
        inorder_print = ""
        postorder_print = ""
        for i in range(len(pre_output)):
            if i < pre_calls:
                preorder_print += pre_output[i]
            elif i < pre_calls + in_calls:
                inorder_print += pre_output[i]
            else:
                postorder_print += pre_output[i]
        reconstructions.append([pre_calls, in_calls, post_calls, preorder_print, inorder_print, postorder_print])
    
    # Sort the reconstructions lexicographically and return the first one
    reconstructions.sort()
    return reconstructions[0]

