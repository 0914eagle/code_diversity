
def x_or_y(n: int, x: int, y: int) -> int:
    
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return y
    else:
        return y
    return x

