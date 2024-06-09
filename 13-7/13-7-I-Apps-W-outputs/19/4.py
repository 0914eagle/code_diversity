
def solve(s, p):
    n = len(s)
    count = [0] * 2
    for i in range(n):
        if s[i] == "d":
            count[0] += 1
        else:
            count[1] += 1
    
    if p >= count[0] + count[1]:
        return n
    
    if p >= count[0]:
        return count[1]
    
    if p >= count[1]:
        return count[0]
    
    return 0

