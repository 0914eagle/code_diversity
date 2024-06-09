
def solve(n, arr):
    signs = ""
    for i in range(n):
        if arr[i] <= 0:
            signs += "+"
        else:
            signs += "-"
    return signs

