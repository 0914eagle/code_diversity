ulate_fun_value(a, b, k):
    return a - ((k - 1) ** 2) * b

def max_total_fun(roller_coasters, visit_durations):
    max_fun_values = []
    for visit_duration in visit_durations:
        max_fun = 0
        for coaster in roller_coasters:
            a, b, t = coaster
            total_fun = 0
            for k in range(1, visit_duration // t + 1):
                fun_value = calculate_fun_value(a, b, k)
                if fun_value <= 0:
                    break
                total_fun += fun_value
            max_fun = max(max_fun, total_fun)
        max_fun_values.append(max_fun)
    return max_fun_values

if __name__ == "__main__":
    N = int(input())
    roller_coasters = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    visit_durations = [int(input()) for _ in range(Q)]

    result = max_total_fun(roller_coasters, visit_durations)
    for fun_value in result:
        print(fun_value)
