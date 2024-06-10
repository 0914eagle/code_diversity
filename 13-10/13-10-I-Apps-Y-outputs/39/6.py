
def check_similarity(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] % 2 == a[j] % 2 or abs(a[i] - a[j]) == 1:
                return True
    return False

def solve(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] % 2 == a[j] % 2 or abs(a[i] - a[j]) == 1:
                return "YES"
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

