
def get_f(p, q, a):
    # find the minimum number of animals among the route areas
    f = min(a[p - 1], a[q - 1])
    return f

def get_average(n, m, a, x, y):
    # calculate the average value of f(p, q) for all pairs p, q (p ≠ q)
    f_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i != j:
                f_sum += get_f(i + 1, j + 1, a)
    return f_sum / (n * (n - 1))

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        x.append(int(input()))
        y.append(int(input()))
    print(get_average(n, m, a, x, y))

if __name__ == '__main__':
    main()

