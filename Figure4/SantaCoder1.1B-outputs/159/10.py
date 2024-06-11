def eat(number, need, remaining):
    
    if number <= 0 or need <= 0 or remaining <= 0:
        return [0, 0]
    if number >= need:
        return [number, 0]
    if number >= remaining:
        return [need, remaining]
    return [number, remaining - need]


