t_permutations(n, x, pos):
    MOD = 10**9 + 7
    left_count = x - 1
    right_count = n - x
    remaining = n - 1

    result = 1
    for i in range(1, n):
        if i < pos:
            result = (result * left_count) % MOD
            left_count -= 1
        elif i > pos:
            result = (result * right_count) % MOD
            right_count -= 1
        else:
            remaining -= 1

    for i in range(2, remaining + 1):
        result = (result * i) % MOD

    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
