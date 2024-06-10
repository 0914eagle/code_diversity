
import math

def get_expected_value(n, k):
    # Calculate the divisors of n
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    
    # Calculate the expected value after k steps
    expected_value = 0
    for divisor in divisors:
        expected_value += divisor * math.pow(divisor, k)
    
    return expected_value

def get_inverse_modulo(a, m):
    # Calculate the inverse of a modulo m
    inv = a
    for i in range(2, m):
        inv = (inv + m - 1) % m
        if inv == 1:
            break
    
    return inv

def get_result(n, k):
    # Calculate the expected value of the number on the blackboard after k steps
    expected_value = get_expected_value(n, k)
    
    # Calculate the inverse of the expected value modulo 10^9 + 7
    inverse = get_inverse_modulo(expected_value, 1000000007)
    
    # Calculate the result as the product of the expected value and its inverse modulo 10^9 + 7
    result = (expected_value * inverse) % 1000000007
    
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_result(n, k))

