
def f1(n, k):
    if n < k:
        return "NO"
    if n % k == 0:
        return "YES"
    if n % 2 == 0:
        return "NO"
    for i in range(1, k+1):
        if n % i == 0:
            return "YES"
    return "NO"

def f2(...):
    ...

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(f1(n, k))

