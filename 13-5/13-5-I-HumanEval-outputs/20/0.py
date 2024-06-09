
def x_or_y(n: int, x: int, y: int) -> int:
    
    # check if n is prime
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n: int) -> bool:
    
    # edge case: 1 is not prime
    if n == 1:
        return False
    # check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

