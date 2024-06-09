
def solve(a):
    n = len(a) // 2
    left, right = a[:n], a[n:]
    if sum(left) == sum(right):
        return "-1"
    return " ".join(map(str, a))

