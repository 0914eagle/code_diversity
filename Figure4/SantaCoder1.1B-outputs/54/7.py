def same_chars(s0: str, s1: str):
    
    if len(s0) != len(s1):
        return False
    return all(s0[i] == s1[i] for i in range(len(s0)))


