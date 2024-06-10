
def get_square_root(n):
    return int(n ** 0.5)

def is_perfect_square(n):
    sqrt = get_square_root(n)
    return sqrt ** 2 == n

def solve(n):
    if is_perfect_square(n):
        return 0
    else:
        return 1

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

