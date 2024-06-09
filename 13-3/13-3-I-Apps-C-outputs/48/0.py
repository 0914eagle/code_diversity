
def count_coprime_pairs(a, b, c, d):
    count = 0
    for x in range(a, b+1):
        for y in range(c, d+1):
            if is_coprime(x, y):
                count += 1
    return count

def is_coprime(x, y):
    return x == 1 or y == 1 or x == -1 or y == -1 or gcd(x, y) == 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

