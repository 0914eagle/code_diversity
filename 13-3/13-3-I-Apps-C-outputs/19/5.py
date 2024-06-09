
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
    
    # Check if the characters in s1 and s2 are present in s in the correct order
    i1 = 0
    i2 = 0
    for i in range(len(s)):
        if i1 < len(s1) and s1[i1] == s[i]:
            i1 += 1
        elif i2 < len(s2) and s2[i2] == s[i]:
            i2 += 1
        else:
            return "no"
    
    return "yes"

