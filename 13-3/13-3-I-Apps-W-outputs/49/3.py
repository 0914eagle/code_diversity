
def solve(n, s, k, a):
    # Find the closest open restaurant to ConneR's office
    closest_open_restaurant = s
    for i in range(s-1, 0, -1):
        if i not in a:
            closest_open_restaurant = i
            break
    for i in range(s+1, n+1):
        if i not in a:
            closest_open_restaurant = i
            break
    
    # Return the minimum number of staircases required to reach the closest open restaurant
    if closest_open_restaurant > s:
        return closest_open_restaurant - s
    else:
        return s - closest_open_restaurant

