def truncate_number(number: float) -> float:
    
    if number == 0:
        return 0
    if number < 0:
        raise ValueError("Number must be positive")
    if number == float("inf"):
        return float("inf")
    if number == float("-inf"):
        return float("-inf")
    if number == float("nan"):
        return float("nan")

    # Find the integer part of the number
    integer_part = math.floor(number)
    # Find the decimal part of the number
    decimal_part = number - integer_part
    # Truncate the decimal part
    decimal_part = math.trunc(decimal_part)
    # Return the integer part and the decimal part
    return integer_part, decimal_part


