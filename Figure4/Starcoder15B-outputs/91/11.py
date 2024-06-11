def is_bored(S):
    
    # Your code here
    boredoms = 0
    for i in range(len(S)):
        if S[i] == 'I':
            boredoms += 1
    return boredoms

