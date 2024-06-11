def is_bored(S):
    
    boredom_count = 0
    for word in S.split('.'):
        for word in word.split('?'):
            for word in word.split('!'):
                if word.strip().startswith('I'):
                    boredom_count += 1
    return boredom_count
