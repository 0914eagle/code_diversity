
def choose_num(x: int, y: int) -> int:
    
    if x > y:
        return -1
    
    for i in range(x, y+1, 2):
        if i % 2 == 0:
            return i
    
    return -1

