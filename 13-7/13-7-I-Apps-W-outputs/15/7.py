
def calculate_mean_exact(a, t, T):
    return (a[t - T + 1] + a[t]) / 2

def calculate_mean_approximate(a, t, T, c):
    mean = 0
    for i in range(t - T + 1, t + 1):
        mean += a[i] / T
    return mean / c

def calculate_relative_error(approx, real):
    return abs(approx - real) / real

def main():
    n, T, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for j in range(m):
        t = p[j]
        real = calculate_mean_exact(a, t, T)
        approx = calculate_mean_approximate(a, t, T, c)
        error = calculate_relative_error(approx, real)
        print(f"{real:.5f} {approx:.5f} {error:.5f}")

if __name__ == '__main__':
    main()

