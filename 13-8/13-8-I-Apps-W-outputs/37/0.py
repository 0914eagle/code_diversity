
def get_max_lit_time(a, M):
    # Find the maximum time when the lamp is lit
    max_time = 0
    for i in range(len(a) - 1):
        max_time = max(max_time, a[i + 1] - a[i])
    max_time = max(max_time, M - a[-1])
    return max_time

def get_optimal_program(a, M):
    # Find the optimal program that maximizes the total time when the lamp is lit
    optimal_program = a
    max_lit_time = get_max_lit_time(a, M)
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            new_program = a[:j] + [a[i] + (a[j] - a[i]) // 2] + a[j + 1:]
            new_lit_time = get_max_lit_time(new_program, M)
            if new_lit_time > max_lit_time:
                optimal_program = new_program
                max_lit_time = new_lit_time
    return optimal_program

def main():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_optimal_program(a, M))

if __name__ == '__main__':
    main()

