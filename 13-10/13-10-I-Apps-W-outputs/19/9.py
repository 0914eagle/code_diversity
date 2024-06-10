
def get_bitwise_and(a, b):
    return a & b

def get_bitwise_or(a, b):
    return a | b

def solve(a, b):
    # Find the minimum possible bitwise OR of all elements in c
    return min([get_bitwise_or(get_bitwise_and(ai, bj), get_bitwise_and(ai, bj+1)) for ai in a for bj in b])

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))

