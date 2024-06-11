

def eat(number, need, remaining):
    
    if number + need > remaining:
        return [remaining + number, 0]
    else:
        return [number + need, remaining - (number + need)]


