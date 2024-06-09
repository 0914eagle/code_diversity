
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
    
    # Initialize the optimal reconstruction with the first fragment
    reconstruction = fragments[0]
    
    # Iterate through the remaining fragments
    for fragment in fragments[1:]:
        # Find the suffix of the current fragment that is equal to a prefix of another fragment
        for suffix in fragment_dict:
            if fragment.startswith(suffix):
                # If the suffix is equal to a prefix of another fragment, add the fragment to the reconstruction
                reconstruction += fragment[len(suffix):]
                break
        else:
            # If no suffix is equal to a prefix of another fragment, the reconstruction is ambiguous
            return "AMBIGUOUS"
    
    return reconstruction

