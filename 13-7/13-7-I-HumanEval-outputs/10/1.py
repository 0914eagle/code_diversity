
def choose_num(x: int, y: int) -> int:
    
    if x > y or x <= 0 or y <= 0:
        return -1
    for num in range(x, y+1):
        if num % 2 == 0:
            return num
    return -1

