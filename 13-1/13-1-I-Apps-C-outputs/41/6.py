
def f1(N, K, items):
    # Initialize a dictionary to store the items available at each store
    available_items = {}
    for i in range(N):
        available_items[i] = set()

    # Add the items to the dictionary
    for i, item in items:
        available_items[i].add(item)

    # Return the dictionary
    return available_items

def f2(N, K, items, bought_items):
    # Initialize a set to store the items that have been bought
    bought_items_set = set()

    # Add the items to the set
    for item in bought_items:
        bought_items_set.add(item)

    # Initialize a list to store the path through the stores
    path = []

    # Iterate through the stores
    for i in range(N):
        # If the current store has an item that has not been bought, add it to the path
        if available_items[i] - bought_items_set:
            path.append(i)
            bought_items_set.add(available_items[i] - bought_items_set)

    # If the path is empty, return "impossible"
    if not path:
        return "impossible"

    # If the path is not empty and there are no items left to buy, return "unique"
    if not bought_items_set:
        return "unique"

    # If the path is not empty and there are still items left to buy, return "ambiguous"
    return "ambiguous"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = []
    for _ in range(K):
        i, item = map(int, input().split())
        items.append((i, item))
    M = int(input())
    bought_items = []
    for _ in range(M):
        bought_items.append(input())
    available_items = f1(N, K, items)
    result = f2(N, K, items, bought_items)
    print(result)

