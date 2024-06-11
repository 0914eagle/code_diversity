def is_bored(S):
    
    count = 0
    for s in S.split('.'):
        s = s.strip()
        if s.startswith('I'):
            count += 1
    return count
