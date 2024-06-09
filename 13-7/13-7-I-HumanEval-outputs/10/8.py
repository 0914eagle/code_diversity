
def choose_num(x: int, y: int) -> int:
    
    for num in range(x, y+1):
        if num % 2 == 0:
            return num
    return -1

