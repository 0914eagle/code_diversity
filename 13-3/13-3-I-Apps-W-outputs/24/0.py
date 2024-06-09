
def plush_toys(x, y):
    if x + y == 1:
        return "Yes"
    elif x + y == 2:
        return "No"
    else:
        if x % 2 == 0 and y % 2 == 0:
            return "Yes"
        else:
            return "No"

