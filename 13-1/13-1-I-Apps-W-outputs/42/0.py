
def get_max_score(a):
    n = len(a) // 3
    a_prime = a[:n] + a[n*2:]
    return sum(a_prime[:n]) - sum(a_prime[n:])

