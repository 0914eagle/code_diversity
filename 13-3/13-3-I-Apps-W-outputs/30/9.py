
def get_kth_smallest_divisor(n, k):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    divisors.sort()
    if k > len(divisors):
        return -1
    return divisors[k - 1]

