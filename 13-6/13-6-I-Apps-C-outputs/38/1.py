
def f(a):
    # Calculate the gcd of the sequence
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd(gcd, a[i])
    return gcd

def f1(n, a):
    # Calculate the number of distinct values of f over the sequence
    values = set()
    for i in range(n):
        for j in range(i+1, n+1):
            values.add(f(a[i:j]))
    return len(values)

def f2(n, a):
    # Calculate the number of distinct values of f over the sequence using a more efficient algorithm
    values = set()
    for i in range(n):
        values.add(f(a[i:]))
    return len(values)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

