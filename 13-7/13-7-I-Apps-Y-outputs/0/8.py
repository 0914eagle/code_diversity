
def is_triangle_possible(sticks):
    sticks = sorted(sticks)
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if sticks[i] + sticks[j] > sticks[k] and sticks[i] + sticks[k] > sticks[j] and sticks[j] + sticks[k] > sticks[i]:
                    return "possible"
    return "impossible"
