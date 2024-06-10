
def get_bitwise_and(a, b):
    return a & b

def get_bitwise_or(c):
    return c

def solve(n, m, a, b):
    c = []
    for i in range(n):
        c.append(get_bitwise_and(a[i], b[i % m]))
    return get_bitwise_or(c)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, a, b))

