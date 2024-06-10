
def calculate_mean_exact(a, p, t):
    return (a[p - t + 1] + a[p] - t + 2 + a[p + 1] + ... + a[p + t - 1]) / t

def calculate_mean_approximate(a, p, t, c):
    mean = 0
    for i in range(p - t + 1, p + 1):
        mean = (mean + a[i] / t) / c
    return mean

def main():
    n, t, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for i in range(m):
        real = calculate_mean_exact(a, p[i], t)
        approx = calculate_mean_approximate(a, p[i], t, c)
        error = abs(approx - real) / real
        print(real, approx, error)

if __name__ == '__main__':
    main()

