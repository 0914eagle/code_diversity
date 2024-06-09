
def get_reconstruction(pre_output, in_output, post_output):
    # Find the possible calls for each routine
    pre_calls = []
    in_calls = []
    post_calls = []
    for i in range(len(pre_output)):
        if pre_output[i] in in_output:
            pre_calls.append("Pre")
        elif pre_output[i] in post_output:
            pre_calls.append("Post")
        else:
            pre_calls.append("In")
    
    for i in range(len(in_output)):
        if in_output[i] in pre_output:
            in_calls.append("Pre")
        elif in_output[i] in post_output:
            in_calls.append("Post")
        else:
            in_calls.append("In")
    
    for i in range(len(post_output)):
        if post_output[i] in pre_output:
            post_calls.append("Pre")
        elif post_output[i] in in_output:
            post_calls.append("In")
        else:
            post_calls.append("Post")
    
    # Find the possible trees for each reconstruction
    reconstructions = []
    for pre_call in pre_calls:
        for in_call in in_calls:
            for post_call in post_calls:
                reconstruction = [pre_call, in_call, post_call]
                reconstructions.append(reconstruction)
    
    # Find the first tree for each reconstruction
    first_trees = []
    for reconstruction in reconstructions:
        pre_call = reconstruction[0]
        in_call = reconstruction[1]
        post_call = reconstruction[2]
        pre_tree = "".join(pre_output)
        in_tree = "".join(in_output)
        post_tree = "".join(post_output)
        if pre_call == "Pre":
            pre_tree = pre_tree[::-1]
        if in_call == "In":
            in_tree = in_tree[::-1]
        if post_call == "Post":
            post_tree = post_tree[::-1]
        first_tree = pre_tree + in_tree + post_tree
        first_trees.append(first_tree)
    
    # Return the reconstruction and the first tree
    return reconstructions, first_trees

if __name__ == '__main__':
    pre_output = input("Enter the preorder output: ")
    in_output = input("Enter the inorder output: ")
    post_output = input("Enter the postorder output: ")
    reconstructions, first_trees = get_reconstruction(pre_output, in_output, post_output)
    for i in range(len(reconstructions)):
        print(reconstructions[i])
        print(first_trees[i])

