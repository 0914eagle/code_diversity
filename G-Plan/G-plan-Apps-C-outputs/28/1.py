
def calculate_additional_sweets(m, k, a, b):
    target_fractions = [ai / sum(a) for ai in a]
    current_counts = [0] * m
    for bi in b:
        current_counts[bi - 1] += 1
    
    max_additional_sweets = float('inf')
    for i in range(m):
        sweets_needed = max(0, int((sum(current_counts) + 1) * target_fractions[i]) - current_counts[i])
        max_additional_sweets = min(max_additional_sweets, sweets_needed)
    
    return max_additional_sweets if max_additional_sweets != float('inf') else "forever"

if __name__ == "__main__":
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = calculate_additional_sweets(m, k, a, b)
    print(result)
