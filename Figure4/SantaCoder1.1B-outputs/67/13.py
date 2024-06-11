def fruit_distribution(s,n):
    
    # your code here
    oranges = 0
    apples = 0
    for i in s:
        if i == 'a':
            apples += 1
        elif i == 'o':
            oranges += 1
    return oranges - apples

