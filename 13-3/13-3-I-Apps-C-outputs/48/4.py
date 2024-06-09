
def count_coprime_pairs(a, b, c, d):
    count = 0
    for i in range(a, b+1):
        for j in range(c, d+1):
            if i != j and __gcd(i, j) == 1:
                count += 1
    return count

