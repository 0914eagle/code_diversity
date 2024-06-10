
def calculate_real_mean(a, t, T):
    return (a[t - T + 1] + a[t] - T + 2 + ... + a[t]) / T

def calculate_approximate_mean(a, t, T, c):
    mean = 0.0
    for i in range(t - T + 1, t + 1):
        mean = (mean + a[i] / T) / c
    return mean

def main():
    n, T, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for j in range(m):
        t = p[j]
        real = calculate_real_mean(a, t, T)
        approx = calculate_approximate_mean(a, t, T, c)
        error = abs(approx - real) / real
        print(real, approx, error)

if __name__ == '__main__':
    main()

