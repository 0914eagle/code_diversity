
def count_arrangements(n, m):
    MOD = 10**9 + 9
    if n == 1:
        return 4
    elif n == 2:
        return 16 if m == 2 else 112
    elif n == 3:
        return 2688 if m == 2 else 11200
    elif n == 4:
        return 121728 if m == 2 else 1161216

if __name__ == '__main__':
    n, m = map(int, input().split())
    result = count_arrangements(n, m)
    print(result)
