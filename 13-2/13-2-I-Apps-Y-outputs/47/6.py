
def solve(n, k):
    if n % 2 == 0:
        # n is even
        if k % 2 == 0:
            # k is even
            return "YES"
        else:
            # k is odd
            return "NO"
    else:
        # n is odd
        if k % 2 == 0:
            # k is even
            return "NO"
        else:
            # k is odd
            return "YES"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

