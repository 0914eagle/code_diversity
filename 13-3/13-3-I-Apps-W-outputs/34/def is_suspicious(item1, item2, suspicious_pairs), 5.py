
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
    
    # Divide items into two groups
    group1 = items[:n//2]
    group2 = items[n//2:]
    
    # Check if any items in group1 are suspicious with any items in group2
    for i in range(len(group1)):
        for j in range(len(group2)):
            if is_suspicious(group1[i], group2[j], suspicious_pairs):
                return [group1[i], group2[j]]
    
    # If no items are suspicious, divide items recursively
    group1_sol = divide_items(group1, suspicious_pairs)
    group2_sol = divide_items(group2, suspicious_pairs)
    return group1_sol + group2_sol

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
    solution = divide_items(items, suspicious_pairs)
    if solution == []:
        print("impossible")
    else:
        print(*solution)

if __name__ == "__main__":
    main()

