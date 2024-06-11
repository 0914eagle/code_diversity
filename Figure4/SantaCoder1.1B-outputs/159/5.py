def eat(number, need, remaining):
    
    if remaining < need:
        return [0, remaining]
    else:
        return [number + need - remaining, remaining]

