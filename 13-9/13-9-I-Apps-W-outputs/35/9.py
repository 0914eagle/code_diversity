
def solve(A, B, C):
    result = 0
    for a in range(1, A+1):
        for b in range(1, B+1):
            for c in range(1, C+1):
                result = (result + a*b*c) % 998244353
    return result

