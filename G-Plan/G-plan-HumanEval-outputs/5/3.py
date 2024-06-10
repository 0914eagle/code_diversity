
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string: str) -> bool:
    length = len(string)
    return is_prime(length)

# Test cases
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
