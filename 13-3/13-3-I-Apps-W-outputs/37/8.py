
def solve(n, a):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(1)
        else:
            result.append(2)
    return result

