
def choose_num(x: int, y: int) -> int:
    
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        raise ValueError("x and y must be positive numbers")
    
    # Check if x is greater than y
    if x > y:
        raise ValueError("x must be less than or equal to y")
    
    # Iterate through the numbers in the range [x, y] inclusive
    for num in range(x, y+1):
        # Check if the number is even
        if num % 2 == 0:
            return num
    
    # If no even number is found, return -1
    return -1

