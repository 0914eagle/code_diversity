
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

    # Initialize a set to store the items that have been visited
    visited_items = set()

    # Start at the first store
    current_store = 0

    # Loop through the items that have been bought
    for item in bought_items:
        # If the item has not been visited before, add it to the path
        if item not in visited_items:
            path.append(item)
            visited_items.add(item)

        # If the item has been visited before, check if it is available at the current store
        else:
            if item in available_items[current_store]:
                path.append(item)
                visited_items.add(item)
                current_store += 1
            else:
                return "impossible"

    # If all items have been visited, return the path
    if len(visited_items) == len(bought_items):
        return "unique"
    else:
        return "ambiguous"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = []
    for i in range(K):
        item = input()
        items.append(item)
    M = int(input())
    bought_items = []
    for i in range(M):
        item = input()
        bought_items.append(item)
    available_items = f1(N, K, items)
    result = f2(N, K, items, bought_items)
    print(result)

