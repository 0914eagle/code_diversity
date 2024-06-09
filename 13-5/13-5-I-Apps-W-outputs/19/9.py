
def get_good_sequences(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i, n):
            x = a[i]
            for k in range(i+1, j+1):
                x ^= a[k]
            if x == 0:
                count += 1
    return count

