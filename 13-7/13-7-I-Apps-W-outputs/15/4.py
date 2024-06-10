
def get_mean_requests(a, T, c):
    mean = 0.0
    for t in range(1, len(a) + 1):
        mean = (mean + a[t - 1] / T) / c
    return mean

def get_mean_requests_approximation(a, T, c):
    mean = 0.0
    for t in range(1, len(a) + 1):
        mean = (mean + a[t - 1] / T) / c
    return mean

def get_relative_error(approx, real):
    return abs(approx - real) / real

def main():
    n, T, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for j in range(m):
        real = sum(a[p[j] - T:p[j]]) / T
        approx = get_mean_requests_approximation(a, T, c)
        error = get_relative_error(approx, real)
        print(f"{real:.5f} {approx:.5f} {error:.5f}")

if __name__ == '__main__':
    main()

