def truncate_number(number: float) -> float:
    
    if number == 0:
        return 0
    if number < 0:
        raise ValueError("Number must be positive")
    if number == 1:
        return 1
    if number < 10:
        return number
    if number < 100:
        return round(number, 1)
    if number < 1000:
        return round(number / 10, 1)
    if number < 10000:
        return round(number / 100, 1)
    if number < 100000:
        return round(number / 1000, 1)
    if number < 1000000:
        return round(number / 10000, 1)
    if number < 10000000:
        return round(number / 100000, 1)
    if number < 100000000:
        return round(number / 1000000, 1)
    if number < 1000000000:
        return round(number / 10000000, 1)
    if number < 10000000000:
        return round(number / 100000000, 1)
    if number < 100000000000:
        return round(number / 1000000000, 1)
    if number < 1000000000000:
        return round(number / 10000000000, 1)
    if number < 10000000000000:
        return round(number / 100000000000, 1)
    if number < 100000000000000:
        return round(number / 1000000000000, 1)
    if number < 1000000000000000:
        return round(number / 10000000