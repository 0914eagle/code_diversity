

def eat(number, need, remaining):
    
    if remaining <= 0:
        return [number, 0]
    elif need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


