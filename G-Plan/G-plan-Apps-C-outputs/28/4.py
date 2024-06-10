
def calculate_additional_sweets(m, k, a, b):
    target_fractions = [ai / sum(a) for ai in a]
    current_counts = [b.count(i) for i in range(1, m + 1)]
    
    additional_sweets = 0
    for i in range(m):
        sweets_needed = max(0, int((sum(current_counts) + additional_sweets) * target_fractions[i]) - current_counts[i])
        additional_sweets += sweets_needed
    
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
