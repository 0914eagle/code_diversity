
def x_or_y(n: int, x: int, y: int) -> int:
    
    # your code here
    return x if is_prime(n) else y

def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

