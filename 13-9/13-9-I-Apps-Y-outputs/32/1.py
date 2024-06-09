
def is_triangle(sticks):
    sticks = sorted(sticks)
    for i in range(len(sticks)-2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return True
    return False

