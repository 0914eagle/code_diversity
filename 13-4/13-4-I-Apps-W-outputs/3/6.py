
def solve(n, line, order):
    line = list(line)
    order = list(order)
    for i in range(n):
        if line[i] != order[i]:
            return "Impossible"
    return "Possible"

