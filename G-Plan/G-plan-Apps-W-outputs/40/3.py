ulate_sum(a, c):
    a.sort()
    n = len(a)
    exclude = n // c
    total_sum = sum(a[exclude:])
    return total_sum

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    result = calculate_sum(a, c)
    print(result