
def solve(n, k):
    if n < k:
        return "NO"
    
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    
    a = [int(n / k)] * k
    for i in range(n % k):
        if parity == "even":
            a[i] += 1
        else:
            a[i] += 2
    
    return "YES\n" + " ".join(map(str, a))

