def truncate_number(number: float) -> float:
    
    if number < 0:
        raise ValueError("Number must be positive.")
    if number == 0:
        return 0
    integer_part = math.floor(number)
    decimals = number - integer_part
    return integer_part, decimals


