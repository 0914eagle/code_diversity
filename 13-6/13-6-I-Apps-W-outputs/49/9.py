
def get_signs(a):
    n = len(a)
    signs = ["+"] * n
    for i in range(1, n):
        if a[i] <= a[i-1]:
            signs[i] = "-"
    return "".join(signs)

