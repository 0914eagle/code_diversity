
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string: str) -> bool:
    return is_prime(len(string))

if __name__ == "__main__":
    input_string = input().strip()
    print(prime_length(input_string))
