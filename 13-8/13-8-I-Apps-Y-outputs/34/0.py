
def get_points(x):
    k = 0
    for i in range(1, x):
        if x % i == 0 and is_prime(i):
            k += 1
    return k

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

