
def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def get_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def get_positive_divisors(n):
    divisors = get_divisors(n)
    positive_divisors = []
    for divisor in divisors:
        if divisor > 0:
            positive_divisors.append(divisor)
    return positive_divisors

def solve(n):
    factorial = get_factorial(n)
    positive_divisors = get_positive_divisors(factorial)
    return len(positive_divisors)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

