
def get_maximum_divisor(n):
    divisor = 1
    while n % divisor == 0:
        divisor += 1
    return divisor - 1

def get_minimum_tax(n):
    maximum_divisor = get_maximum_divisor(n)
    return maximum_divisor

def get_optimal_split(n):
    optimal_split = []
    while n > 0:
        maximum_divisor = get_maximum_divisor(n)
        optimal_split.append(maximum_divisor)
        n -= maximum_divisor
    return optimal_split

def get_minimum_tax_with_optimal_split(n):
    optimal_split = get_optimal_split(n)
    minimum_tax = 0
    for part in optimal_split:
        minimum_tax += get_maximum_divisor(part)
    return minimum_tax

if __name__ == '__main__':
    n = int(input())
    print(get_minimum_tax_with_optimal_split(n))

