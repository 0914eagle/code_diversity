def is_bored(S):
    
    count = 0
    for s in S.split("."):
        if s.strip().startswith("I"):
            count += 1
    return count
