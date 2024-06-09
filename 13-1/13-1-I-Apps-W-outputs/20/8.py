
def get_common_divisors(a, b):
    common_divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    return common_divisors

def get_coprime_divisors(a, b, common_divisors):
    coprime_divisors = []
    for i in common_divisors:
        if is_coprime(i, a) and is_coprime(i, b):
            coprime_divisors.append(i)
    return coprime_divisors

def is_coprime(a, b):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def get_max_divisors(a, b):
    common_divisors = get_common_divisors(a, b)
    coprime_divisors = get_coprime_divisors(a, b, common_divisors)
    return len(coprime_divisors)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_max_divisors(a, b))

