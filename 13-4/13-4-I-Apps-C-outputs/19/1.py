
def get_reconstruction(pre_print, in_print, post_print):
    # Find the two calls to prePrint in the observed output
    pre_print_calls = [i for i, c in enumerate(pre_print) if c == "P"]
    # Find the two calls to inPrint in the observed output
    in_print_calls = [i for i, c in enumerate(in_print) if c == "I"]
    # Find the two calls to postPrint in the observed output
    post_print_calls = [i for i, c in enumerate(post_print) if c == "P"]

    # Create a list of all possible reconstructions
    reconstructions = []
    for pre_call_1 in pre_print_calls:
        for pre_call_2 in pre_print_calls:
            for in_call_1 in in_print_calls:
                for in_call_2 in in_print_calls:
                    for post_call_1 in post_print_calls:
                        for post_call_2 in post_print_calls:
                            # Check if the reconstruction is valid
                            if pre_call_1 != pre_call_2 and in_call_1 != in_call_2 and post_call_1 != post_call_2:
                                # Create a list of the calls in the order Pre, In, Post
                                calls = ["Pre", "In", "Post"]
                                calls[pre_call_1] = "Pre"
                                calls[pre_call_2] = "Pre"
                                calls[in_call_1] = "In"
                                calls[in_call_2] = "In"
                                calls[post_call_1] = "Post"
                                calls[post_call_2] = "Post"
                                # Add the reconstruction to the list of possible reconstructions
                                reconstructions.append(calls)

    # Sort the reconstructions lexicographically
    reconstructions.sort()

    # Return the first reconstruction
    return reconstructions[0]

