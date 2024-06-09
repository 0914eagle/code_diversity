
def solve(S, P, k):
    if k < 1 or k > 4:
        return "NO"
    if S < k or P < 1:
        return "NO"
    
    for i in range(1, S+1):
        for j in range(1, S-i+1):
            prod = i * j
            if prod == P:
                return str(i) + " " + str(j)
    
    return "NO"

