
def solve(s, p):
    n = len(s)
    count = [0] * 2
    for i in range(n):
        if s[i] == "d":
            count[0] += 1
        else:
            count[1] += 1
    
    if count[0] > count[1]:
        count[0], count[1] = count[1], count[0]
    
    if count[0] == 0:
        return n
    
    if count[1] == 0:
        return 0
    
    if p >= count[0]:
        return n - count[0]
    
    if p >= count[1]:
        return n - count[1]
    
    if count[0] - count[1] > p:
        return n - count[0] + p
    
    return n - count[1] - (count[0] - count[1] - p)

