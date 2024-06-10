ulate_fun(a, b, t):
    fun_values = []
    for k in range(1, t + 1):
        fun_value = a - (k - 1) ** 2 * b
        if fun_value <= 0:
            break
        fun_values.append(fun_value)
    return sum(fun_values)

def max_total_fun(N, coasters, Q, visit_durations):
    max_fun_values = []
    for T in visit_durations:
        total_fun = 0
        for i in range(N):
            total_fun += calculate_fun(coasters[i][0], coasters[i][1], T // coasters[i][2])
        max_fun_values.append(total_fun)
    return max_fun_values

if __name__ == "__main__":
    N = int(input())
    coasters = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    visit_durations = [int(input()) for _ in range(Q)]

    result = max_total_fun(N, coasters, Q, visit_durations)
    for fun_value in result:
        print(fun_value)
""