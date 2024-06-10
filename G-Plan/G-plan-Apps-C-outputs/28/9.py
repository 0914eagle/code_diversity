
def calculate_additional_sweets(m, k, a, b):
    target_fractions = [ai / sum(a) for ai in a]
    current_counts = [b.count(i) for i in range(1, m + 1)]
    additional_sweets = 0

    for i in range(m):
        min_count = target_fractions[i] * k - current_counts[i]
        max_count = target_fractions[i] * k + 1 - current_counts[i]
        additional_sweets = max(additional_sweets, max(0, min_count))

    return additional_sweets

if __name__ == "__main__":
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = calculate_additional_sweets(m, k, a, b)
    print(result)
