
def plush_toys(x, y):
    if x + y == 1:
        return "Yes"
    if x + y < 3:
        return "No"
    if x == 0:
        return "Yes"
    if x % 2 == 0 and y % 2 == 0:
        return "Yes"
    return "No"

