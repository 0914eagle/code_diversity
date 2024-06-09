
def renumber_items(n, items):
    items = list(set(items))
    items.sort()
    result = [0] * len(items)
    for i, item in enumerate(items):
        result[i] = items.index(item) + 1
    return result

