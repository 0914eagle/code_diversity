def fruit_distribution(s,n):
    
    # your code here
    s = s.split()
    apples = int(s[0])
    oranges = int(s[1])
    mango = int(s[2])
    return mango - apples - oranges

