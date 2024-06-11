

def is_bored(S):
    
    boredoms = 0
    for sentence in S.split('.'):
        if sentence.startswith('I'):
            boredoms += 1
    for sentence in S.split('?'):
        if sentence.startswith('I'):
            boredoms += 1
    for sentence in S.split('!'):
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms


