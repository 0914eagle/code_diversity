
def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def get_minimum_bitwise_or(a, b):
    return min(bitwise_or(bitwise_and(ai, bj), bj) for ai in a for bj in b)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_minimum_bitwise_or(a, b))

if __name__ == '__main__':
    main()

