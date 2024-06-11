def eat(number, need, remaining):
    
    if number < 0 or need < 0 or remaining < 0:
        return [0, 0]
    if number == 0:
        return [need, remaining]
    if need == 0:
        return [number, 0]
    if remaining == 0:
        return [number, 0]
    if number < need:
        return [number, remaining]
    if number > need:
        return [need, remaining]
    if number == need:
        return [need, remaining]
    if number == need + 1:
        return [need, remaining]
    if number == need + 2:
        return [need, remaining]
    if number == need + 3:
        return [need, remaining]
    if number == need + 4:
        return [need, remaining]
    if number == need + 5:
        return [need, remaining]
    if number == need + 6:
        return [need, remaining]
    if number == need + 7:
        return [need, remaining]
    if number == need + 8:
        return [need, remaining]
    if number == need + 9:
        return [need, remaining]
    if number == need + 10:
        return [need, remaining]
    if number == need + 11:
        return [need, remaining]
    if number == need + 12:
        return [need, remaining]
    if number == need + 13:
        return [need, remaining]
    if number == need + 14:
        return [need, remaining]
    if number == need + 15:
        return [need, remaining]
    if number == need + 16:
        return [need, remaining]
    if number == need + 17:
        return [need, remaining]
    if number == need + 18:
        return [need, remaining]
    if number == need + 19:
        return [need, remaining]
    if number == need + 20:
        return [need, remaining]
    if number == need + 21:
        return [need, remaining]
    if number == need + 22:
        return [need, remaining]
    if number == need + 23:
        return [need, remaining]
    if number == need + 24:
        return [need, remaining]
    if number == need