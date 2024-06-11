def is_bored(S):
    
    count = 0
    for i in S.split():
        if i == "I":
            count += 1
    return count

