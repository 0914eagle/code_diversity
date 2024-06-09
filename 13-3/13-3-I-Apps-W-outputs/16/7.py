
def get_maximum_quality_matching(student_names, pseudonyms):
    # Initialize a dictionary to store the relevance of each pseudonym to each student
    relevance = {}
    for student in student_names:
        relevance[student] = {}
        for pseudonym in pseudonyms:
            relevance[student][pseudonym] = get_lcp(student, pseudonym)
    
    # Initialize a list to store the optimal matching
    matching = []
    
    # Loop through each student and find the pseudonym with the highest relevance
    for student in student_names:
        max_relevance = 0
        optimal_pseudonym = ""
        for pseudonym in pseudonyms:
            if relevance[student][pseudonym] > max_relevance:
                max_relevance = relevance[student][pseudonym]
                optimal_pseudonym = pseudonym
        matching.append((student, optimal_pseudonym))
    
    # Remove the optimal pseudonym from the list of pseudonyms
    pseudonyms.remove(optimal_pseudonym)
    
    # Recursively call the function to find the next optimal matching
    if len(student_names) > 1:
        get_maximum_quality_matching(student_names, pseudonyms)
    
    # Return the optimal matching
    return matching

def get_lcp(str1, str2):
    # Find the length of the longest common prefix of the two strings
    lcp = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            lcp += 1
        else:
            break
    return lcp

