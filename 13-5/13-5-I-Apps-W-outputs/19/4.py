
def get_good_pairs(a):
    n = len(a)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            x = a[i]
            y = a[j]
            while x != y:
                x = (x ^ (x & -x)) | y
                y = (y ^ (y & -y)) | x
            if x == 0:
                pairs += 1
    return pairs

