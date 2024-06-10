
def get_bitwise_or(a, b):
    return a | b

def get_bitwise_and(a, b):
    return a & b

def get_minimum_bitwise_or(a, b):
    return min(get_bitwise_or(x, y) for x in a for y in b)

def solve(n, m, a, b):
    c = [get_bitwise_and(x, y) for x in a for y in b]
    return get_minimum_bitwise_or(c, c[1:])

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, a, b))

