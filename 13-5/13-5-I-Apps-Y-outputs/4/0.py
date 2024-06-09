
def solve(N, L, drawers):
    items = {}
    for i in range(N):
        item = i + 1
        drawer_a, drawer_b = drawers[i]
        if drawer_a not in items:
            items[drawer_a] = item
        elif drawer_b not in items:
            items[drawer_b] = item
        else:
            items[drawer_a] = item
            items[drawer_b] = None
    
    result = []
    for i in range(N):
        item = i + 1
        drawer_a, drawer_b = drawers[i]
        if items[drawer_a] == item:
            result.append("LADICA")
        elif items[drawer_b] == item:
            result.append("LADICA")
        else:
            result.append("SMECE")
    
    return result

