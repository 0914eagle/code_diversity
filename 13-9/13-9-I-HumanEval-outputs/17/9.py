
def iscube(a: int) -> bool:
    
    if a == 0:
        return True
    for i in range(1, int(a**(1/3) + 1)):
        if a == i**3:
            return True
    return False

