def eat(number, need, remaining):
    
    if remaining < need - number:
        return [number + remaining, 0]
    else:
        return [number + need, remaining - need]


if