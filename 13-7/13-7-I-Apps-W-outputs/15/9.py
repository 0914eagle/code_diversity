
def calculate_mean_brute_force(a, p, T):
    return sum(a[p-T+1:p+1]) / T

def calculate_mean_exponential_decay(a, p, T, c):
    mean = 0
    for t in range(p-T+1, p+1):
        mean = (mean + a[t] / T) / c
    return mean

def main():
    n, T, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for j in range(m):
        real = calculate_mean_brute_force(a, p[j], T)
        approx = calculate_mean_exponential_decay(a, p[j], T, c)
        error = abs(approx-real) / real
        print(f"{real:.5f} {approx:.5f} {error:.5f}")

if __name__ == '__main__':
    main()

