
def get_max_files(x, y):
    n = len(x)
    m = len(y)
    total_x = sum(x)
    total_y = sum(y)
    if total_x != total_y:
        return 0
    x.sort()
    y.sort()
    max_files = 0
    for i in range(n):
        for j in range(m):
            if x[i] + y[j] <= total_x:
                max_files += 1
    return max_files

