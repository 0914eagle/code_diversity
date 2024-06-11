def fruit_distribution(s,n):
    
    apples = 0
    oranges = 0
    mango = 0
    for i in range(n):
        if s[i] == 'a':
            apples += 1
        elif s[i] == 'o':
            oranges += 1
        elif s[i] == 'm':
            mango += 1
    return apples - oranges + mango

