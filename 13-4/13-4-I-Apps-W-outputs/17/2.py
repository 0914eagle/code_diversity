
def get_input():
    n = int(input())
    return n

def get_initial_array(n):
    return [i for i in range(1, n+1)] + [i for i in range(1, n+1)]

def get_distance(a, i):
    x = a.index(i)
    y = a.index(i, x+1)
    return y - x

def get_sum(a):
    n = len(a) // 2
    return sum(n - i * abs(get_distance(a, i) + i - n) for i in range(1, n+1))

def solve(n):
    a = get_initial_array(n)
    min_sum = get_sum(a)
    while True:
        for i in range(n):
            x = a.index(i+1)
            y = a.index(i+1, x+1)
            if x < y:
                a[x], a[y] = a[y], a[x]
                break
        else:
            break
        sum_after_swap = get_sum(a)
        if sum_after_swap < min_sum:
            min_sum = sum_after_swap
        else:
            a[x], a[y] = a[y], a[x]
    return a

def main():
    n = get_input()
    a = solve(n)
    print(*a)

if __name__ == '__main__':
    main()

