
def is_possible(breads, order):
    # Convert the permutations to lists
    breads = list(map(int, breads.split()))
    order = list(map(int, order.split()))
    
    # Check if the breads can be sorted in the desired order
    if breads == order:
        return "Possible"
    
    # Check if the breads can be sorted by rotating them in groups of 3
    for i in range(len(breads) - 2):
        if breads[i:i+3] == order[i:i+3]:
            return "Possible"
    
    # If the breads cannot be sorted, return "Impossible"
    return "Impossible"

