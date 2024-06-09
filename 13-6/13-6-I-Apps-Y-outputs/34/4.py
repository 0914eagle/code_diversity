
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

def get_number_of_positive_divisors(n):
    positive_divisors = get_positive_divisors(n)
    return len(positive_divisors)

def main():
    n = int(input())
    print(get_number_of_positive_divisors(n))

if __name__ == '__main__':
    main()

