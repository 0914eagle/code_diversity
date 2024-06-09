
def solve(oranges, apples):
    if oranges == 0 and apples == 0:
        return "Impossible"
    if oranges == 1 and apples == 1:
        return "AB"
    if oranges == 1 and apples > 1:
        return "A" + "B" * (apples - 1)
    if oranges > 1 and apples == 1:
        return "B" + "A" * (oranges - 1)
    if oranges > 1 and apples > 1:
        return "A" + "B" * (apples - 1) + "A" * (oranges - 1)

