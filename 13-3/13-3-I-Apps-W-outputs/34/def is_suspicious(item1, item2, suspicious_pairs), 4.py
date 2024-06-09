
def is_suspicious(item1, item2, suspicious_pairs):
    for pair in suspicious_pairs:
        if item1 == pair[0] and item2 == pair[1] or item1 == pair[1] and item2 == pair[0]:
            return True
    return False

def divide_items(items, suspicious_pairs):
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if not is_suspicious(items[i], items[j], suspicious_pairs):
                return [items[i], items[j]]
    return "impossible"

items = input().split()
suspicious_pairs = []
for i in range(int(input())):
    suspicious_pairs.append(input().split())

result = divide_items(items, suspicious_pairs)
if result == "impossible":
    print("impossible")
else:
    print(result[0])
    print(result[1])

