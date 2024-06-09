
def is_possible(x, y):
    if x + y == 1:
        return "Yes"
    if x + y == 0:
        return "No"
    if x == 0:
        return "Yes"
    if y == 0:
        return "No"
    if x % 2 == 0 and y % 2 == 0:
        return "Yes"
    if x % 2 == 1 and y % 2 == 1:
        return "No"
    if x % 2 == 0 and y % 2 == 1:
        return "Yes"
    if x % 2 == 1 and y % 2 == 0:
        return "No"

