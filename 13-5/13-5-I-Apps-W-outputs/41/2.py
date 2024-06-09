
def solve(s, p, k):
    for i in range(1, s+1):
        for j in range(1, s-i+1):
            if i*j == p and i+j == s:
                return f"{i} {j}"
    return "NO"

