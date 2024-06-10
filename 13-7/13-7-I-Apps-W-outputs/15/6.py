
def calculate_mean(a_list, t, c):
    mean = 0
    for i in range(t, len(a_list)):
        mean = (mean + a_list[i] / t) / c
    return mean

def calculate_mean_approx(a_list, t, c):
    mean = 0
    for i in range(t, len(a_list)):
        mean = (mean + a_list[i] / t) / c
    return mean

def main():
    n, t, c = map(int, input().split())
    a_list = list(map(int, input().split()))
    m = int(input())
    p_list = list(map(int, input().split()))

    for p in p_list:
        real = sum(a_list[p-t+1:p+1]) / t
        approx = calculate_mean_approx(a_list, t, c)
        error = abs(approx-real) / real
        print(f"{real:.5f} {approx:.5f} {error:.5f}")

if __name__ == '__main__':
    main()

