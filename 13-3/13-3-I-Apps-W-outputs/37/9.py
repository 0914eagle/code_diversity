
def solve(n, a):
    result = []
    for i in range(n):
        if a[i] == 1:
            result.append(2)
        else:
            result.append(1)
    return result

