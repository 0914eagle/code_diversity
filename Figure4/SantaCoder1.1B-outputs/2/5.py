def truncate_number(number: float) -> float:
    
    if number < 0:
        raise ValueError("Number must be positive")
    if number == 0:
        return 0
    # Find the integer part
    integer = math.floor(number)
    # Find the decimal part
    decimal = number - integer
    return decimal


