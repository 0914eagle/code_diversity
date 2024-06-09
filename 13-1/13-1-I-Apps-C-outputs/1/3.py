
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
    for i in range(1, len(fragments)):
        # Get the current fragment and its suffix
        fragment = fragments[i]
        suffix = fragment[-5:]
        
        # Check if the suffix is in the dictionary and if it is equal to the prefix of the previous fragment
        if suffix in fragment_dict and fragment_dict[suffix][0][:5] == reconstruction[-5:]:
            # If it is, add the fragment to the reconstruction and remove it from the dictionary
            reconstruction += fragment[5:]
            fragment_dict[suffix].pop(0)
            if not fragment_dict[suffix]:
                del fragment_dict[suffix]
        else:
            # If it is not, the reconstruction is ambiguous
            return "AMBIGUOUS"
    
    # Return the optimal reconstruction
    return reconstruction

