def is_bored(S):
    
    return sum(1 for s in S.split('.') if s.strip().startswith('I'))

