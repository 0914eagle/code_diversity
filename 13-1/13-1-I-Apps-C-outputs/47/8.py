
def gcd_table_to_array(gcd_table):
    n = int(len(gcd_table)**0.5)
    a = [0] * n
    for i in range(n):
        for j in range(n):
            if gcd_table[i*n+j] > a[i]:
                a[i] = gcd_table[i*n+j]
    return a

