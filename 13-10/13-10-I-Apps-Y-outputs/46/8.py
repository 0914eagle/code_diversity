
def find_max_multiple(x, y, n):
    for i in range(n, 0, -1):
        if i % x == y:
            return i
    return 0

def find_max_multiple_v2(x, y, n):
    return n - (n % x) + y

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, y, n = map(int, input().split())
        print(find_max_multiple_v2(x, y, n))

