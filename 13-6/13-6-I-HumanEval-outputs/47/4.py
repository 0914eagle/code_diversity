
def x_or_y(n: int, x: int, y: int) -> int:
    
    # Your code here
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

