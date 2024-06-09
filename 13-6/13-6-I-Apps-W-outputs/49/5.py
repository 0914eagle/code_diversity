
def solve(n, arr):
    signs = ["+"] * n
    signs[0] = "-"
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            signs[i] = "-"
    return "".join(signs)

