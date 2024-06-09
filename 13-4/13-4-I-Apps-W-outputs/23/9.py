
def solve(a):
    if a == 0:
        return "yes"
    if a == 1:
        return "yes"
    if a == 2:
        return "no"
    if a == 3:
        return "yes"
    if a % 3 == 0:
        return "yes"
    return "no"

