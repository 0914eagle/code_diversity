def eat(number, need, remaining):
    
    if remaining >= need - number:
        return [need, remaining - (need - number)]
    else:
        return [number + remaining, 0]


if