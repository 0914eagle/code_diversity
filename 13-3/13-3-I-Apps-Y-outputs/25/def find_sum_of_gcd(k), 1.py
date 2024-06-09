
def find_sum_of_gcd(k):
    sum = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                sum += gcd(a, b, c)
    return sum

