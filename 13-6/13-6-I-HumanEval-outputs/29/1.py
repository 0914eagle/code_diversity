
def triangle_area(a: int, b: int, c: int) -> float:
    
    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)
    else:
        return -1

