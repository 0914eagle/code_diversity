def eat(number, need, remaining):
    
    if number < need:
        return [0, number]
    else:
        return [number - need, remaining]

