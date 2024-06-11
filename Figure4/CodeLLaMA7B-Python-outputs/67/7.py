def fruit_distribution(s,n):
    
    apples, oranges = s.split()
    apples = int(apples.split(" ")[0])
    oranges = int(oranges.split(" ")[0])
    return n - apples - oranges

if