def eat(number, need, remaining):
    
    if number + remaining < need:
        return [number + remaining, 0]
    else:
        return [need, remaining - (need - number)]


if