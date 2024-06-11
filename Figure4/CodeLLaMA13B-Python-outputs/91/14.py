def is_bored(S):
    
    count = 0
    for i in S.split('.') + S.split('?') + S.split('!'):
        if i.strip().startswith('I'):
            count += 1
    return count
