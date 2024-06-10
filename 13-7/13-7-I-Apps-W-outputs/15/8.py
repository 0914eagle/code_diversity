
def calculate_mean_exact(a, T):
    return sum(a) / T

def calculate_mean_approximate(a, T, c):
    mean = 0
    for t in range(len(a)):
        mean = (mean + a[t] / T) / c
    return mean

def main():
    n, T, c = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for j in range(m):
        real = calculate_mean_exact(a[p[j]-T+1:p[j]+1], T)
        approx = calculate_mean_approximate(a[p[j]-T+1:p[j]+1], T, c)
        error = abs(approx-real) / real
        print(real, approx, error)

if __name__ == '__main__':
    main()

