
def find_nearest_fraction(x, y, n):
    min_diff = float('inf')
    min_fraction = ''
    for b in range(1, n+1):
        a = round(x*b/y)
        diff = abs(x/y - a/b)
        if diff < min_diff:
            min_diff = diff
            min_fraction = f'{a}/{b}'
    return min_fraction

