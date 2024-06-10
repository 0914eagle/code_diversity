
def get_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_minimum_prime_number_greater_than_or_equal_to(x):
    prime_numbers = get_prime_numbers(x)
    for prime in prime_numbers:
        if prime >= x:
            return prime
    return None

if __name__ == '__main__':
    x = int(input())
    result = get_minimum_prime_number_greater_than_or_equal_to(x)
    if result:
        print(result)
    else:
        print(-1)

