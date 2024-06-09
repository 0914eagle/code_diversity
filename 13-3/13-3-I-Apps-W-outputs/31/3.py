
def get_initial_arrangement(n, x, a):
    arrangement = [0] * n
    for i in range(n):
        if i < x:
            arrangement[i] = a[i] - a[x]
        elif i == x:
            arrangement[i] = a[i]
        else:
            arrangement[i] = a[i] - a[x - 1]
    return arrangement

