
def is_suspicious(item1, item2, suspicious_pairs):
    for pair in suspicious_pairs:
        if item1 == pair[0] and item2 == pair[1] or item1 == pair[1] and item2 == pair[0]:
            return True
    return False

def divide_items(items, suspicious_pairs):
    # Initialize the lists to store the items to buy
    walter_items = []
    jesse_items = []

    # Iterate through the items and check if they are suspicious
    for item in items:
        is_suspicious_item = is_suspicious(item, items, suspicious_pairs)
        if is_suspicious_item:
            walter_items.append(item)
        else:
            jesse_items.append(item)

    # Check if there are any items left to buy
    if len(walter_items) == 0 or len(jesse_items) == 0:
        return "impossible"

    # Return the lists of items to buy
    return walter_items, jesse_items

