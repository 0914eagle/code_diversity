
def solve(m, n, p, q):
    if m < n or m > 1000000 or n > 1000000 or p > 1000000 or q > 1000000:
        return "IMPOSSIBLE"
    
    for i in range(100000, 1000000):
        num = str(i)
        if len(num) != m:
            continue
        if num[:n] == "0" * n:
            continue
        if num[n:] == "0" * (m - n):
            continue
        if int(num[n:]) * q != int(num[:n] + p):
            continue
        return num
    
    return "IMPOSSIBLE"

