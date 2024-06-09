
def verify_claim(s, s1, s2):
    if len(s) != len(s1) + len(s2):
        return "no"
    
    s1_indices = [i for i, c in enumerate(s1) if c in s]
    s2_indices = [i for i, c in enumerate(s2) if c in s]
    
    for i in range(len(s1_indices)):
        for j in range(i+1, len(s1_indices)):
            if s1_indices[i] > s1_indices[j]:
                return "no"
    
    for i in range(len(s2_indices)):
        for j in range(i+1, len(s2_indices)):
            if s2_indices[i] > s2_indices[j]:
                return "no"
    
    return "yes"

