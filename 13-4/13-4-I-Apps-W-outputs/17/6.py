
def get_input():
    n = int(input())
    return n

def get_permuted_array(n):
    a = list(range(1, n+1))
    a += a
    return a

def get_distance(a, i):
    x_i = a.index(i)
    y_i = a.index(i, x_i+1)
    return y_i - x_i

def get_sum(a):
    n = len(a) // 2
    return sum((n - i) * abs(get_distance(a, i) + i - n) for i in range(1, n+1))

def solve(n):
    a = get_permuted_array(n)
    return a

if __name__ == '__main__':
    n = get_input()
    a = solve(n)
    print(*a)

