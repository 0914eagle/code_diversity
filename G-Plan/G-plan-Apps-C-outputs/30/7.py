
def count_valid_arrangements(n, m):
    MOD = 10**9 + 9
    if n == 1:
        return 4
    elif n == 2:
        return (16 ** (m // 2)) % MOD
    else:
        return 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = count_valid_arrangements(n, m)
    print(result)
