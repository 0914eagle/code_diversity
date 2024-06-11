def eat(number, need, remaining):
    
    if number < need:
        return [0, number]
    else:
        return [need - number, remaining]

