def eat(number, need, remaining):
    
    if need > remaining:
        return [number + remaining, 0]
    else:
        return [number + need, remaining - need]


