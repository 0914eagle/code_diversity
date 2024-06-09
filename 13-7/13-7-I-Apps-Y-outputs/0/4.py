
def is_triangle(sticks):
    sticks.sort()
    return sticks[0] + sticks[1] > sticks[2]

