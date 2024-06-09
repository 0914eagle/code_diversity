
def choose_num(x: int, y: int) -> int:
    
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        return -1
    
    # Find the biggest even integer in the range [x, y] inclusive
    for num in range(x, y+1):
        if num % 2 == 0:
            return num
    
    # If no even integer is found, return -1
    return -1

