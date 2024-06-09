
def get_initial_arrangement(n, x, a):
    arrangement = [0] * n
    for i in range(n):
        if i + 1 == x:
            arrangement[i] = a[i] - 1
        else:
            arrangement[i] = a[i]
    return arrangement

