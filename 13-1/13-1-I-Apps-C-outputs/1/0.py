
def reconstruct_text(fragments):
    # Sort the fragments by length in descending order
    fragments.sort(key=len, reverse=True)
    
    # Create a dictionary to store the fragments and their suffixes
    fragment_dict = {}
    for fragment in fragments:
        suffix = fragment[-5:]
        if suffix not in fragment_dict:
            fragment_dict[suffix] = [fragment]
        else:
            fragment_dict[suffix].append(fragment)
    
    # Create a list to store the optimal reconstruction
    reconstruction = []
    
    # Iterate through the fragments and add them to the reconstruction
    while fragments:
        # Find the fragment with the longest suffix that is also a prefix of another fragment
        for suffix in fragment_dict:
            if len(fragment_dict[suffix]) == 1:
                continue
            fragment = fragment_dict[suffix][0]
            fragment_dict[suffix] = fragment_dict[suffix][1:]
            reconstruction.append(fragment)
            fragments.remove(fragment)
            break
    
    # If there are still fragments left, the reconstruction is ambiguous
    if fragments:
        return "AMBIGUOUS"
    
    # Concatenate the fragments in the optimal order
    optimal_reconstruction = "".join(reconstruction)
    return optimal_reconstruction

