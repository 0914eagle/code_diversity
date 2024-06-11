def is_bored(S):
    
    count = 0
    for s in S.split('.'):
        for s in s.split('?'):
            for s in s.split('!'):
                if s.strip().startswith('I'):
                    count += 1
    return count
