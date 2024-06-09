
def solve(n, k):
    if n < k:
        return "NO"
    
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    
    a = [0] * k
    a[0] = n
    for i in range(1, k):
        if parity == "even":
            a[i] = a[i-1] - 1
        else:
            a[i] = a[i-1] + 1
    
    if a[k-1] < 0:
        return "NO"
    
    return "YES\n" + " ".join(str(x) for x in a)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

