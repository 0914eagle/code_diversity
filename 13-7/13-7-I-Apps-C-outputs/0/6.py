
def solve(m, n, p, q):
    if m < n or n < 1 or p < 1 or q < 1:
        return "IMPOSSIBLE"
    
    num = 10**(m-1) + 1
    while num <= 10**m:
        if str(num)[n:] == str(num%10)[1:] and str(num)[:n] != "0":
            result = int(str(num)[:n] + str(p) + str(num)[n:]) * q
            if result == num:
                return str(num)
        num += 1
    
    return "IMPOSSIBLE"

