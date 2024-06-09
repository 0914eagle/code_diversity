
def is_suspicious(item1, item2, suspicious_pairs):
    for pair in suspicious_pairs:
        if item1 == pair[0] and item2 == pair[1] or item1 == pair[1] and item2 == pair[0]:
            return True
    return False

def divide_items(items, suspicious_pairs):
    n = len(items)
    if n == 0:
        return []
    if n == 1:
        return [items[0]]
    if n == 2:
        if is_suspicious(items[0], items[1], suspicious_pairs):
            return [items[0], items[1]]
        else:
            return [items[0]]
    
    # Divide the items into two groups
    group1 = items[:n//2]
    group2 = items[n//2:]
    
    # Check if either group contains a suspicious pair
    for i in range(len(group1)):
        for j in range(len(group2)):
            if is_suspicious(group1[i], group2[j], suspicious_pairs):
                return [group1[i]] + divide_items(group1[:i] + group1[i+1:] + group2, suspicious_pairs)
            if is_suspicious(group2[j], group1[i], suspicious_pairs):
                return [group2[j]] + divide_items(group1 + group2[:j] + group2[j+1:], suspicious_pairs)
    
    # If no suspicious pair is found, return both groups
    return divide_items(group1, suspicious_pairs) + divide_items(group2, suspicious_pairs)

def main():
    n = int(input())
    items = []
    for i in range(n):
        items.append(input())
    m = int(input())
    suspicious_pairs = []
    for i in range(m):
        pair = input().split()
        suspicious_pairs.append(pair)
    result = divide_items(items, suspicious_pairs)
    if result == []:
        print("impossible")
    else:
        print(*result[0], sep="\n")
        print(*result[1], sep="\n")

if __name__ == "__main__":
    main()

