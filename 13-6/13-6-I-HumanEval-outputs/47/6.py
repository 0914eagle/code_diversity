
def x_or_y(n: int, x: int, y: int) -> int:
    
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

