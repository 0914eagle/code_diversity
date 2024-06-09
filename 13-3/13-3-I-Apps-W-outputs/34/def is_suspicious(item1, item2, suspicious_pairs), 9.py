
def is_suspicious(item1, item2, suspicious_pairs):
    for pair in suspicious_pairs:
        if item1 == pair[0] and item2 == pair[1] or item1 == pair[1] and item2 == pair[0]:
            return True
    return False

def divide_items(items, suspicious_pairs):
    # Initialize the lists to store the items to be bought by Walter and Jesse
    walter_items = []
    jesse_items = []

    # Iterate through the items and check if they are suspicious with any other item
    for item in items:
        is_suspicious_with_any = False
        for other_item in items:
            if is_suspicious(item, other_item, suspicious_pairs):
                is_suspicious_with_any = True
                break
        # If the item is not suspicious with any other item, add it to the list of items to be bought by the person who will go to the store next
        if not is_suspicious_with_any:
            if len(walter_items) < len(jesse_items):
                walter_items.append(item)
            else:
                jesse_items.append(item)

    # If both lists have the same number of items, return the lists
    if len(walter_items) == len(jesse_items):
        return walter_items, jesse_items
    else:
        return "impossible"

