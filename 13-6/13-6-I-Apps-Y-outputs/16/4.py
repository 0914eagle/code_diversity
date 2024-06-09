
def solve(p):
    n = len(p)
    a = [0] * n
    for i in range(n):
        a[i] = p.index(i)
    return a

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        a = solve(p)
        print(*a)

if __name__ == '__main__':
    main()

