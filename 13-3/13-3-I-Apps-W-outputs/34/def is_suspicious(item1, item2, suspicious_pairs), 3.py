
def is_suspicious(item1, item2, suspicious_pairs):
    for pair in suspicious_pairs:
        if item1 == pair[0] and item2 == pair[1] or item1 == pair[1] and item2 == pair[0]:
            return True
    return False

def divide_items(items, suspicious_pairs):
    n = len(items)
    if n == 0:
        return []
    
    # Initialize the first item as the first element of the first list
    list1 = [items[0]]
    list2 = []
    
    for i in range(1, n):
        item = items[i]
        if is_suspicious(list1[-1], item, suspicious_pairs):
            list2.append(item)
        else:
            list1.append(item)
    
    return list1, list2

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
    
    list1, list2 = divide_items(items, suspicious_pairs)
    print(*list1)
    print(*list2)

if __name__ == "__main__":
    main()

