
def find_min_f(a):
    n = len(a)
    min_f = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                f = (i-j)**2 + g(i, j, a)**2
                if f < min_f:
                    min_f = f
    return min_f

def g(i, j, a):
    if i > j:
        i, j = j, i
    sum = 0
    for k in range(i, j+1):
        sum += a[k]
    return sum

