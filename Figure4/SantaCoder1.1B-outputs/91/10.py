def is_bored(S):
    
    return sum(1 for word in S.split() if word.startswith('I'))


