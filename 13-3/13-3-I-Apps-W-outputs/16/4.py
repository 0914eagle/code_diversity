
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
    
    # Initialize a list to store the optimal matching
    matching = []
    
    # Iterate over the sorted dictionary
    for name, (pseudonym, lcp) in mapping:
        # If the pseudonym is not already in the matching, add it
        if pseudonym not in [p[1] for p in matching]:
            matching.append((name, pseudonym))
    
    # Return the maximum quality of matching and the optimal matching
    return len(matching), matching

