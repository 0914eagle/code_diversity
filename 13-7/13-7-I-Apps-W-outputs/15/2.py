
def get_real_mean(a, t, T):
    return (a[t - T + 1] + a[t]) / 2

def get_approx_mean(a, t, T, c):
    mean = 0
    for i in range(t - T + 1, t + 1):
        mean = (mean + a[i] / T) / c
    return mean

def get_error(real, approx):
    return abs(approx - real) / real

def main():
    n, T, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for j in range(m):
        t = p[j]
        real = get_real_mean(a, t, T)
        approx = get_approx_mean(a, t, T, c)
        error = get_error(real, approx)
        print(f"{real:.5f} {approx:.5f} {error:.5f}")

if __name__ == '__main__':
    main()

