
def pistol_shooting(n, a):
    # Calculate the minimum number of shots required to knock each can down
    shots = [0] * n
    for i in range(n):
        for j in range(i):
            shots[i] += a[j] * (i - j)
    shots = [x + 1 for x in shots]
    
    # Return the minimum number of shots and the order of indices of cans
    return min(shots), list(range(1, n + 1))

