
def calculate_additional_sweets(m, k, a, b):
    target_fractions = [ai / sum(a) for ai in a]
    sweet_counts = [0] * m
    for bi in b:
        sweet_counts[bi - 1] += 1

    max_additional_sweets = float('inf')
    for i in range(m):
        sweets_needed = max(0, int(target_fractions[i] * (sum(sweet_counts) + max_additional_sweets) - sweet_counts[i]) - 1)
        max_additional_sweets = min(max_additional_sweets, sweets_needed)

    return max_additional_sweets if max_additional_sweets != float('inf') else 'forever'

if __name__ == "__main__":
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(calculate_additional_sweets(m, k, a, b))
