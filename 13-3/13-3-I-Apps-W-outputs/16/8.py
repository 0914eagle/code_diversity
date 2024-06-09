
def solve(names, pseudonyms):
    # Initialize a dictionary to store the mapping of students to pseudonyms
    mapping = {}
    
    # Iterate over the names and pseudonyms
    for name, pseudonym in zip(names, pseudonyms):
        # Find the longest common prefix between the name and pseudonym
        lcp = 0
        for i in range(min(len(name), len(pseudonym))):
            if name[i] == pseudonym[i]:
                lcp += 1
            else:
                break
        
        # Add the mapping to the dictionary
        mapping[name] = (pseudonym, lcp)
    
    # Sort the dictionary by the length of the longest common prefix in descending order
    mapping = sorted(mapping.items(), key=lambda x: x[1][1], reverse=True)
    
    # Initialize the maximum quality of matching
    max_quality = 0
    
    # Iterate over the sorted dictionary
    for name, (pseudonym, lcp) in mapping:
        # If the current student has not been matched yet, match them to the current pseudonym
        if name not in mapping.values():
            mapping[name] = pseudonym
            max_quality += lcp
    
    # Return the maximum quality of matching and the mapping
    return max_quality, mapping

