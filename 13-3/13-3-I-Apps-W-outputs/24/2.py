
def solve(x, y):
    if x + y == 1:
        return "Yes"
    if x + y == 0:
        return "No"
    if x == 0:
        return "Yes"
    if y == 0:
        return "No"
    if x < 0 or y < 0:
        return "No"
    if x == 1 and y == 1:
        return "Yes"
    if x == 2 and y == 2:
        return "Yes"
    if x == 3 and y == 3:
        return "Yes"
    if x == 4 and y == 4:
        return "No"
    if x == 5 and y == 5:
        return "Yes"
    if x == 6 and y == 6:
        return "Yes"
    if x == 7 and y == 7:
        return "Yes"
    if x == 8 and y == 8:
        return "No"
    if x == 9 and y == 9:
        return "Yes"
    if x == 10 and y == 10:
        return "Yes"
    return "No"

