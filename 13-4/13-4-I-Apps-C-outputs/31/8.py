
def get_reconstructions(pre_output, in_output, post_output):
    # Initialize a list to store the reconstructions
    reconstructions = []
    
    # Iterate over all possible combinations of Pre, In, and Post calls
    for pre_calls in combinations(["Pre", "In", "Post"], 2):
        for in_calls in combinations(["Pre", "In", "Post"], 2):
            for post_calls in combinations(["Pre", "In", "Post"], 2):
                # Check if the current combination of calls generates the observed outputs
                if check_outputs(pre_calls, in_calls, post_calls, pre_output, in_output, post_output):
                    # If it does, add the reconstruction to the list
                    reconstructions.append((pre_calls, in_calls, post_calls))
    
    # Return the list of reconstructions
    return reconstructions

def check_outputs(pre_calls, in_calls, post_calls, pre_output, in_output, post_output):
    # Initialize a dictionary to store the calls and their corresponding outputs
    calls = {
        "Pre": pre_calls,
        "In": in_calls,
        "Post": post_calls
    }
    
    # Initialize a list to store the outputs
    outputs = []
    
    # Iterate over the calls and their corresponding outputs
    for call, output in calls.items():
        # Check if the current call generates the observed output
        if output in [pre_output, in_output, post_output]:
            # If it does, add the output to the list
            outputs.append(output)
    
    # Return True if all three outputs are present in the list, False otherwise
    return len(outputs) == 3

def get_first_tree(pre_output, in_output, post_output):
    # Initialize a list to store the possible trees
    trees = []
    
    # Iterate over all possible reconstructions
    for pre_calls, in_calls, post_calls in get_reconstructions(pre_output, in_output, post_output):
        # Check if the current reconstruction generates the observed outputs
        if check_outputs(pre_calls, in_calls, post_calls, pre_output, in_output, post_output):
            # If it does, add the tree to the list
            trees.append((pre_calls, in_calls, post_calls))
    
    # Return the first tree in the list, if any
    return trees[0] if trees else None

if __name__ == '__main__':
    pre_output = input("Preorder output: ")
    in_output = input("Inorder output: ")
    post_output = input("Postorder output: ")
    
    print("Reconstructions:")
    for pre_calls, in_calls, post_calls in get_reconstructions(pre_output, in_output, post_output):
        print(f"{pre_calls} {in_calls} {post_calls}")
    
    print("First tree:")
    pre_calls, in_calls, post_calls = get_first_tree(pre_output, in_output, post_output)
    print(f"Preorder: {pre_calls}")
    print(f"Inorder: {in_calls}")
    print(f"Postorder: {post_calls}")

