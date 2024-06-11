def is_bored(S):
    
    return sum(1 for w in S.split() if w.startswith('I'))

