
def get_max_quality_matching(student_names, pseudonyms):
    # Initialize a dictionary to store the relevance of each pseudonym to each student
    relevance = {}
    for i, student in enumerate(student_names):
        relevance[i] = {}
        for j, pseudonym in enumerate(pseudonyms):
            # Calculate the length of the largest common prefix between the student name and the pseudonym
            lcp = 0
            for k in range(min(len(student), len(pseudonym))):
                if student[k] == pseudonym[k]:
                    lcp += 1
                else:
                    break
            relevance[i][j] = lcp
    
    # Initialize a dictionary to store the matching between students and pseudonyms
    matching = {}
    
    # Loop through the students and pseudonyms and find the maximum quality matching
    for i in range(len(student_names)):
        # Find the pseudonym with the maximum relevance to the current student
        max_relevance = 0
        for j in range(len(pseudonyms)):
            if relevance[i][j] > max_relevance:
                max_relevance = relevance[i][j]
                matching[i] = j
    
    return matching

