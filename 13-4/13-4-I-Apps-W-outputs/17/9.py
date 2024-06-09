
def get_input():
    n = int(input())
    return n

def get_permuted_array(n):
    a = list(range(1, n+1))
    b = a[:]
    for i in range(n):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        a[x], a[y] = a[y], a[x]
    return a

def get_distance_sum(a):
    s = 0
    for i in range(n):
        x = a.index(i+1)
        y = a.index(i+1, x+1)
        d = y - x
        s += (n-i) * abs(d + i - n)
    return s

def solve(n):
    a = get_permuted_array(n)
    s = get_distance_sum(a)
    return a

if __name__ == '__main__':
    n = get_input()
    a = solve(n)
    print(*a)

