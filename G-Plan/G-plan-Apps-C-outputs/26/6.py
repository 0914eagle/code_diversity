ulate_fun_value(a, b, k):
    return a - ((k - 1) ** 2) * b

def max_fun_value(coasters, visit_time):
    dp = [0] * (visit_time + 1)
    for coaster in coasters:
        a, b, t = coaster
        for i in range(visit_time, t - 1, -1):
            dp[i] = max(dp[i], dp[i - t] + calculate_fun_value(a, b, (visit_time - i) // t + 1))
    return dp[visit_time]

if __name__ == "__main__":
    N = int(input())
    coasters = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    for _ in range(Q):
        T = int(input())
        print(max_fun_value(coasters, T)