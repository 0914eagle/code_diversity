
def is_triangle(sticks):
    
    sticks.sort()
    if len(sticks) < 3:
        return "impossible"
    if sticks[0] + sticks[1] > sticks[2]:
        return "possible"
    return "impossible"

