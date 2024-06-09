
def solve(s, p, k):
    if k < 1 or k > 4:
        return "NO"
    if s < k or p < 1:
        return "NO"
    
    for i in range(1, s+1):
        for j in range(1, s-i+1):
            if i * j == p:
                return "NO"
    
    for i in range(1, s+1):
        for j in range(1, s-i+1):
            for k in range(1, s-i-j+1):
                if i + j + k == s and i * j * k == p:
                    return str(i) + " " + str(j) + " " + str(k)
    
    return "NO"

