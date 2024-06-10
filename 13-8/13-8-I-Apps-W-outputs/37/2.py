
def get_max_lit_time(a, M):
    # Find the maximum time when the lamp is lit
    max_time = 0
    for i in range(len(a) - 1):
        max_time = max(max_time, a[i + 1] - a[i])
    max_time = max(max_time, M - a[-1])
    return max_time

def alter_program(a, M):
    # Alter the program to maximize the total time when the lamp is lit
    n = len(a)
    if n == 1:
        return a
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Insert a[i] between a[i] and a[j]
            new_a = a[:i] + [a[i]] + a[i:j] + [a[j]] + a[j + 1:]
            if get_max_lit_time(new_a, M) > get_max_lit_time(a, M):
                a = new_a
                break
    return a

def main():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_lit_time(alter_program(a, M), M))

if __name__ == '__main__':
    main()

