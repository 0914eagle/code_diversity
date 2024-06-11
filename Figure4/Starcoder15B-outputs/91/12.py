def is_bored(S):
    
    count = 0
    for word in S.split():
        if word == 'I':
            count += 1
    return count

