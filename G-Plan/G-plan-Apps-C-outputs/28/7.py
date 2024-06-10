
def calculate_additional_sweets(m, k, a, b):
    target_fractions = [ai / sum(a) for ai in a]
    sweet_counts = [0] * m
    for bi in b:
        sweet_counts[bi - 1] += 1

    additional_sweets = 0
    for i in range(m):
        sweets_needed = round(target_fractions[i] * sum(sweet_counts))
        additional_sweets = max(additional_sweets, sweets_needed - sweet_counts[i])

    return additional_sweets

if __name__ == "__main__":
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = calculate_additional_sweets(m, k, a, b)
    if result == 0:
        print("forever")
    else:
        print(result)
