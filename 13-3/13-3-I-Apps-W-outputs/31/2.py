
def get_initial_arrangement(n, x, a):
    arrangement = [0] * n
    for i in range(n):
        if i + 1 == x:
            arrangement[i] = a[i] - 1
        else:
            arrangement[i] = a[i]
    
    for i in range(n):
        if arrangement[i] > 0:
            for j in range(i + 1, n):
                if arrangement[j] > 0:
                    arrangement[j] -= 1
    
    return arrangement

