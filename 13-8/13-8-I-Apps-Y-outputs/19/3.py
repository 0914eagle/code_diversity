
def max_value_of_x(S):
    x = 0
    max_x = 0
    for i in S:
        if i == "I":
            x += 1
        else:
            x -= 1
        max_x = max(max_x, x)
    return max_x

