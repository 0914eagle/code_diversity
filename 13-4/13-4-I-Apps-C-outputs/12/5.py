
def get_max_points(a):
    n = len(a)
    points = 0
    for i in range(n):
        if a[i] != 1:
            points += a[i]
            for j in range(i+1, n):
                if a[j] == a[i]-1 or a[j] == a[i]+1:
                    points += a[j]
                    a[j] = 0
    return points

