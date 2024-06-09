
def restore_array(n, gcd_table):
    a = [0] * n
    for i in range(n):
        a[i] = 1
    for i in range(n):
        for j in range(i+1, n):
            gcd = gcd_table[i*n+j]
            for k in range(n):
                if a[k] % gcd != 0:
                    a[k] *= gcd
    return a

