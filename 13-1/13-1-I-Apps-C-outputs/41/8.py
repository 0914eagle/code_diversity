
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

    # Iterate through the items available at each store
    for i in range(N):
        # If the current store has an item that has not been bought, add it to the path
        if available_items[i] - bought_items_set:
            path.append(i)
            bought_items_set.add(available_items[i] - bought_items_set)

    # If the path is not empty, return it
    if path:
        return path
    # Otherwise, return "impossible"
    else:
        return "impossible"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = [input().split() for _ in range(K)]
    bought_items = input().split()
    available_items = f1(N, K, items)
    path = f2(N, K, items, bought_items)
    print(path)

