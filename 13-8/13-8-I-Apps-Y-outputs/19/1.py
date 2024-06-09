
def solve(x, s):
    max_value = 0
    for i in s:
        if i == "I":
            x += 1
        else:
            x -= 1
        max_value = max(max_value, x)
    return max_value

