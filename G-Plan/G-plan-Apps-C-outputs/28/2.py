
def calculate_additional_sweets(m, k, a, b):
    target_fractions = [ai / sum(a) for ai in a]
    sweet_counts = [0] * m
    for bi in b:
        sweet_counts[bi - 1] += 1

    additional_sweets = 0
    for i in range(m):
        min_sweets = target_fractions[i] * sum(sweet_counts) - 1
        max_sweets = target_fractions[i] * sum(sweet_counts) + 1
        if sweet_counts[i] < min_sweets:
            additional_sweets = max(additional_sweets, min_sweets - sweet_counts[i])

    return additional_sweets

if __name__ == "__main__":
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = calculate_additional_sweets(m, k, a, b)
    print(result)
