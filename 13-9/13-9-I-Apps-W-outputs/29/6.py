
def get_gcd(a, b):
    if a == 0:
        return b
    return get_gcd(b % a, a)

def get_divisors(a, b):
    divisors = []
    for i in range(a, b+1):
        if i % get_gcd(a, b) == 0:
            divisors.append(i)
    return divisors

def get_biggest_divisor(divisors):
    return max(divisors)

if __name__ == '__main__':
    a, b = map(int, input().split())
    divisors = get_divisors(a, b)
    print(get_biggest_divisor(divisors))

