
def choose_num(x: int, y: int) -> int:
    
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        raise ValueError("x and y must be positive")

    # Check if x is greater than y
    if x > y:
        raise ValueError("x must be less than or equal to y")

    # Iterate from x to y and find the biggest even number
    for num in range(x, y+1):
        if num % 2 == 0:
            return num

    # If no even number is found, return -1
    return -1

