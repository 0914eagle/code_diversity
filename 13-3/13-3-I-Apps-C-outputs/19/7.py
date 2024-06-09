
def verify_answers(s, s1, s2):
    # Check if the length of the merged string is correct
    if len(s) != len(s1) + len(s2):
        return "no"
    
    # Check if the indices of the characters in s1 are in ascending order
    for i in range(len(s1) - 1):
        if s1[i] > s1[i + 1]:
            return "no"
    
    # Check if the indices of the characters in s2 are in ascending order
    for i in range(len(s2) - 1):
        if s2[i] > s2[i + 1]:
            return "no"
    
    # Check if the characters in s1 and s2 are in the correct order in s
    for i in range(len(s1)):
        if s[i] != s1[i]:
            return "no"
    for i in range(len(s2)):
        if s[i + len(s1)] != s2[i]:
            return "no"
    
    return "yes"

