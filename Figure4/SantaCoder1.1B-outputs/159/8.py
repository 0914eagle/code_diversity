def eat(number, need, remaining):
    
    if number < 0 or need < 0 or remaining < 0:
        return [0, 0]
    if number == 0:
        return [need, remaining]
    if need == 0:
        return [number, 0]
    if remaining == 0:
        return [0, 0]
    return [eat(number-need, need, remaining-need), number-need]

