def is_bored(S):
    
    return len([w for w in S.split('.') if w.startswith('I')])


