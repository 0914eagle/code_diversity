
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def solve(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if is_similar(a[i], a[j]):
                return "YES"
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

