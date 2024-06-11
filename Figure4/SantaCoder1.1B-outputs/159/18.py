def eat(number, need, remaining):
    
    if number < need:
        return [0, number]
    elif number > need:
        return [number - need, 0]
    else:
        return [number - need, number]

