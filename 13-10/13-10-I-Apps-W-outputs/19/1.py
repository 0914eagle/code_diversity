
def get_bitwise_and(a, b):
    return a & b

def get_bitwise_or(a, b):
    return a | b

def solve(a, b):
    result = 0
    for i in range(len(a)):
        result = get_bitwise_or(result, get_bitwise_and(a[i], b[0]))
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))

