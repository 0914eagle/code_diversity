
def is_triangle(sticks):
    sticks.sort()
    if sticks[0] + sticks[1] > sticks[2]:
        return True
    else:
        return False

