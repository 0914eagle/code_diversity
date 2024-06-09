
N = int(input())
items = [input() for _ in range(N)]
M = int(input())
suspicious_pairs = [input().split() for _ in range(M)]

# Create a dictionary to store the suspicious pairs
suspicious_dict = {}
for pair in suspicious_pairs:
    item1, item2 = pair
    suspicious_dict[item1] = item2
    suspicious_dict[item2] = item1

# Initialize sets for Walter and Jesse's items
walter_items = set()
jesse_items = set()

# Iterate through the items and assign them to Walter or Jesse
for item in items:
    if item not in walter_items and item not in jesse_items:
        if item in suspicious_dict:
            pair_item = suspicious_dict[item]
            if pair_item not in walter_items and pair_item not in jesse_items:
                walter_items.add(item)
                jesse_items.add(pair_item)
        else:
            walter_items.add(item)

# Check if all items are assigned
if len(walter_items) + len(jesse_items) == len(items):
    print('\n'.join(walter_items))
    print('\n'.join(jesse_items))
else:
    print("impossible")
