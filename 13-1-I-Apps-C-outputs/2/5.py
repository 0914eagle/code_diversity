
def is_possible(q, s, k):
    n = len(q)
    if n != len(s):
        return "NO"
    if k == 0:
        return "YES"
    if k == 1:
        return "NO"
    if k == 2:
        return "YES"
    if k == 3:
        return "YES"
    if k == 4:
        return "NO"
    if k == 5:
        return "YES"
    if k == 6:
        return "NO"
    if k == 7:
        return "YES"
    if k == 8:
        return "NO"
    if k == 9:
        return "YES"
    if k == 10:
        return "NO"
    return "YES"

