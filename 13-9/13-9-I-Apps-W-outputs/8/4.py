
def max_messiness(n, k):
    if k == 0:
        return 0
    if n == 1:
        return 0
    if k == 1:
        return n - 1
    if k == 2:
        return n
    if k == 3:
        return n + 1
    if k == 4:
        return n + 2
    if k == 5:
        return n + 3
    if k == 6:
        return n + 4
    if k == 7:
        return n + 5
    if k == 8:
        return n + 6
    if k == 9:
        return n + 7
    if k == 10:
        return n + 8


