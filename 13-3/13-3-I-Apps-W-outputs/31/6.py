
def get_initial_arrangement(n, x, a):
    arrangement = [0] * n
    for i in range(n):
        arrangement[i] += a[i]
    for i in range(n):
        if x == i:
            break
        x = (x + 1) % n
        arrangement[x] -= 1
    return arrangement

