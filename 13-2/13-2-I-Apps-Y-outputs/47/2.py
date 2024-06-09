
def solve(n, k):
    if n < k:
        return "NO"
    
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    
    a = [int(n / k) for _ in range(k)]
    if parity == "even":
        a[0] += n % k
    else:
        a[0] += 1
    
    return "YES\n" + " ".join(str(x) for x in a)

