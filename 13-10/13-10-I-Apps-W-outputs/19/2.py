
def get_min_bitwise_or(a, b):
    return min(a | b for a, b in zip(a, b))

def solve(n, m, a, b):
    return get_min_bitwise_or(a, b)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, a, b))

