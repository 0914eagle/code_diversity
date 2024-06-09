
def solve(N, L, pairs):
    # Initialize a dictionary to store the items and their corresponding drawers
    items = {}
    
    # Iterate through each item and its corresponding drawers
    for i in range(1, N+1):
        A, B = pairs[i-1]
        
        # If the first drawer is empty, store the item in that drawer
        if A not in items:
            items[A] = i
        
        # If the second drawer is empty, store the item in that drawer
        elif B not in items:
            items[B] = i
        
        # If both drawers are filled, try to move the item from the first drawer to its other drawer
        else:
            item = items.pop(A)
            if B not in items:
                items[B] = item
            else:
                items[A] = item
    
    # Iterate through the items and determine where they will be stored or thrown away
    result = []
    for i in range(1, N+1):
        if i in items:
            result.append("LADICA")
        else:
            result.append("SMECE")
    
    return result

