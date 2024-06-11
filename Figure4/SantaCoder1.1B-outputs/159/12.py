def eat(number, need, remaining):
    
    if number < need:
        return [number, 0]
    else:
        return [number - need, remaining]

