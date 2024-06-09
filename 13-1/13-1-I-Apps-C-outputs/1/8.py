
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
        
        # Check if the suffix is in the dictionary
        if suffix in fragment_dict:
            # Get the list of fragments with the same suffix
            fragments_with_suffix = fragment_dict[suffix]
            
            # Check if the current fragment is in the list
            if fragment in fragments_with_suffix:
                # Remove the current fragment from the list
                fragments_with_suffix.remove(fragment)
                
                # Add the fragment to the reconstruction
                reconstruction += fragment
                
                # Update the dictionary with the new list of fragments
                fragment_dict[suffix] = fragments_with_suffix
    
    return reconstruction

