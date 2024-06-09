
def get_reconstruction(pre_output, in_output, post_output):
    # Initialize a list to store the reconstruction
    reconstruction = []
    
    # Iterate through the pre_output and find the corresponding calls in the prePrint routine
    for char in pre_output:
        if char in pre_output:
            reconstruction.append("Pre")
        elif char in in_output:
            reconstruction.append("In")
        elif char in post_output:
            reconstruction.append("Post")
    
    # Iterate through the in_output and find the corresponding calls in the inPrint routine
    for char in in_output:
        if char in pre_output:
            reconstruction.append("Pre")
        elif char in in_output:
            reconstruction.append("In")
        elif char in post_output:
            reconstruction.append("Post")
    
    # Iterate through the post_output and find the corresponding calls in the postPrint routine
    for char in post_output:
        if char in pre_output:
            reconstruction.append("Pre")
        elif char in in_output:
            reconstruction.append("In")
        elif char in post_output:
            reconstruction.append("Post")
    
    # Return the reconstruction
    return reconstruction

