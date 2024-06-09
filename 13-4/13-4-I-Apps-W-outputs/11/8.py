
def get_maximum_divisor(n):
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            n = n // divisor
        else:
            divisor += 1
    return n

def get_minimum_tax(n):
    return get_maximum_divisor(n)

def get_optimal_split(n):
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            n = n // divisor
        else:
            divisor += 1
    return n

if __name__ == '__main__':
    n = int(input())
    print(get_minimum_tax(n))

