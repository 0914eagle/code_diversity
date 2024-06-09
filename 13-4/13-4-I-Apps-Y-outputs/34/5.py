
def is_triangle_possible(sticks):
    sticks.sort()
    for i in range(len(sticks)-2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return "possible"
    return "impossible"

