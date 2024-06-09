
def is_suspicious_pair(item1, item2, suspicious_pairs):
    return (item1, item2) in suspicious_pairs or (item2, item1) in suspicious_pairs

def divide_items(items, suspicious_pairs):
    walter_items = []
    jesse_items = []
    for item in items:
        if is_suspicious_pair(item, walter_items[-1], suspicious_pairs):
            jesse_items.append(item)
        else:
            walter_items.append(item)
    return walter_items, jesse_items

def main():
    num_items = int(input())
    items = []
    for i in range(num_items):
        items.append(input())
    num_suspicious_pairs = int(input())
    suspicious_pairs = []
    for i in range(num_suspicious_pairs):
        pair = input().split()
        suspicious_pairs.append((pair[0], pair[1]))
    walter_items, jesse_items = divide_items(items, suspicious_pairs)
    print(*walter_items)
    print(*jesse_items)

if __name__ == "__main__":
    main()

