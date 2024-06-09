
def get_good_sequences(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            xor = a[i]
            for k in range(i+1, j):
                xor ^= a[k]
            if xor == 0:
                count += 1
    return count

