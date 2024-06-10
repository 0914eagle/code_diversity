
def get_bitwise_and(a, b):
    return a & b

def get_bitwise_or(a, b):
    return a | b

def solve(a, b):
    c = [get_bitwise_and(ai, bj) for ai in a for bj in b]
    return get_bitwise_or(*c)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))

