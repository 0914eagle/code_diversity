
def calculate_fun(a, b, t):
    fun_values = []
    for k in range(1, t + 1):
        fun = a - (k - 1) ** 2 * b
        if fun > 0:
            fun_values.append(fun)
        else:
            break
    return sum(fun_values)

def max_total_fun(N, coasters, Q, visit_durations):
    max_fun_values = []
    for T in visit_durations:
        max_fun = 0
        for i in range(2 ** N):
            total_fun = 0
            total_time = 0
            for j in range(N):
                if i & (1 << j):
                    total_time += coasters[j][2]
                    if total_time <= T:
                        total_fun += calculate_fun(coasters[j][0], coasters[j][1], coasters[j][2])
                    else:
                        break
            max_fun = max(max_fun, total_fun)
        max_fun_values.append(max_fun)
    return max_fun_values

if __name__ == "__main__":
    N = int(input())
    coasters = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    visit_durations = [int(input()) for _ in range(Q)]

    result = max_total_fun(N, coasters, Q, visit_durations)
    for fun_value in result:
        print(fun_value)
