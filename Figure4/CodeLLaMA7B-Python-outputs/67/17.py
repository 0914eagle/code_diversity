def fruit_distribution(s,n):
    
    apples, oranges = s.split(" ")
    apples = int(apples.split("apples")[0])
    oranges = int(oranges.split("oranges")[0])
    return n - apples - oranges

if