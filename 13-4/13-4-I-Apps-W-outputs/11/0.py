
def get_maximum_divisor(n):
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
        else:
            divisor += 1
    return n

def get_minimum_tax(n):
    divisors = []
    while n > 1:
        divisors.append(get_maximum_divisor(n))
        n //= divisors[-1]
    return sum(divisors)

if __name__ == '__main__':
    n = int(input())
    print(get_minimum_tax(n))

