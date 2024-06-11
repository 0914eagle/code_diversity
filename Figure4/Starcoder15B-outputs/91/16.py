def is_bored(S):
    
    boredoms = 0
    for word in S.split():
        if word == "I":
            boredoms += 1
    return boredoms

