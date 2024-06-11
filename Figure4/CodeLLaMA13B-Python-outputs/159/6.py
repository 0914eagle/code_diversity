def eat(number, need, remaining):
    
    if remaining < need:
        return [remaining + number, 0]
    else:
        return [remaining + number, remaining - need]


if