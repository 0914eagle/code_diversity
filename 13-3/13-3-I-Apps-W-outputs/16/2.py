
def solve(names, pseudonyms):
    # Initialize a dictionary to store the mapping of students to pseudonyms
    mapping = {}
    
    # Loop through each student and pseudonym
    for student, pseudonym in zip(names, pseudonyms):
        # Find the longest common prefix between the student's name and the pseudonym
        lcp = 0
        for i in range(min(len(student), len(pseudonym))):
            if student[i] == pseudonym[i]:
                lcp += 1
            else:
                break
        
        # Add the student to the dictionary with their corresponding pseudonym and LCP value
        mapping[student] = (pseudonym, lcp)
    
    # Sort the dictionary by the LCP value in descending order
    mapping = sorted(mapping.items(), key=lambda x: x[1][1], reverse=True)
    
    # Create a list to store the optimal matching
    matching = []
    
    # Loop through the sorted dictionary and add the students to the matching list
    for student, (pseudonym, lcp) in mapping:
        matching.append((student, pseudonym))
    
    # Return the matching list
    return matching

