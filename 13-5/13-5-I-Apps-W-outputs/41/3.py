
def solve(s, p, k):
    if k < 1 or k > 4:
        return "NO"
    if s < k or p < 1:
        return "NO"
    for i in range(1, s+1):
        for j in range(1, s-i+1):
            if i + j == s and i * j == p:
                return str(i) + " " + str(j)
    return "NO"

