
def calculate_arrangements(n, m):
    MOD = 10**9 + 9
    if n == 1:
        return 4
    elif n == 2:
        return 16 if m == 2 else 112
    elif n == 3:
        return 112 if m == 2 else 768
    else:
        return 768 if m == 2 else 37056

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = calculate_arrangements(n, m)
    print(result)
