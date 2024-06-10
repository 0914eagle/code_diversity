
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def solve(a):
    n = len(a)
    if n % 2 == 1:
        return "NO"
    for i in range(0, n, 2):
        x, y = a[i], a[i+1]
        if not is_similar(x, y):
            return "NO"
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == '__main__':
    main()

